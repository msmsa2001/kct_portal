import json
import uuid
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from kct_portal import settings
from django.views.decorators.csrf import csrf_exempt
from .models import BeneficiaryData, Donation, EventMaster, GalleryItem, GovtSchemeMaster, HomeBannerMaster, KCTEnquireMaster, PartnerLogo, ProjectImage, ProjectMaster, SystemMaster,SystemMasterCategory, BeneficiaryCategory, ManagingListCategoryMaster, ListItemCategory, BeneficiaryCategory
from .utils import get_data_afillat, get_data_dict, get_data_dict_aid, get_data_dict_casestdy, get_data_dict_Event, get_data_dict_term_and_condition, get_gallery_images, get_data_about_page, get_data_activies,get_data_benefits, get_data_career, get_footer_data,convert_to_k_format
from django.contrib import messages
from django.core.mail import send_mail
# from django.http import JsonResponse
from django.conf import settings
# import razorpay
import requests
from collections import defaultdict
from .utils import send_receipt_email
from .utils import generate_receipt_number
from django.utils.timezone import now



@csrf_exempt
def create_cashfree_order(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    data = request.POST
    amount = float(data.get("amount", 0))

    if amount <= 0:
        return JsonResponse({"error": "Invalid amount"}, status=400)

    order_id = f"ORD-{uuid.uuid4().hex[:12]}"

    donation = Donation.objects.create(
        name=f"{data.get('first_name')} {data.get('last_name')}",
        email=data.get("email"),
        mobile=data.get("mobile"),
        amount=amount,
        message = data.get("message"),
        donation_type=data.get("type"),

        address=data.get("address"),
        city=data.get("city"),
        state=data.get("state"),
        pincode=data.get("pincode"),
        country=data.get("country"),

        pan_number=data.get("pan"),

        order_id=order_id,
    )

    if settings.CASHFREE_ENV == "PROD":
        url = "https://api.cashfree.com/pg/orders"
    else:
        url = "https://sandbox.cashfree.com/pg/orders"

    headers = {
        "Content-Type": "application/json",
        "x-client-id": settings.CASHFREE_APP_ID,
        "x-client-secret": settings.CASHFREE_SECRET_KEY,
        "x-api-version": "2023-08-01",
    }

    payload = {
        "order_id": order_id,
        "order_amount": amount,
        "order_currency": "INR",
        "customer_details": {
            "customer_id": f"cust_{donation.id}",  # ✅ IMPORTANT
            "customer_name": donation.name,
            "customer_email": donation.email,
            "customer_phone": donation.mobile,
        },
        "order_meta": {
            "return_url": f"https://khidmattrust.org/payment-success/?order_id={order_id}"
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    result = response.json()

    if response.status_code != 200:
        print("Cashfree Error:", result)
        return JsonResponse(result, status=response.status_code)

    donation.payment_session_id = result["payment_session_id"]
    donation.save()

    return JsonResponse({
        "payment_session_id": result["payment_session_id"]
    })


@csrf_exempt
def cashfree_webhook(request):
    payload = json.loads(request.body)

    order = payload.get("data", {}).get("order", {})
    payment = payload.get("data", {}).get("payment", {})

    order_id = order.get("order_id")
    status = payment.get("payment_status")
    transaction_id = payment.get("cf_payment_id")
    payment_method_data = payment.get("payment_method", {})

    if not order_id:
        return JsonResponse({"status": "ignored"})

    donation = Donation.objects.filter(order_id=order_id).first()
    if not donation:
        return JsonResponse({"status": "not found"})

    # 🔒 Idempotency check
    if donation.payment_status == "SUCCESS":
        return JsonResponse({"status": "already processed"})

    if status == "SUCCESS":
        donation.payment_status = "SUCCESS"
        donation.transaction_id = transaction_id

        if isinstance(payment_method_data, dict) and payment_method_data:
            method = list(payment_method_data.keys())[0]
            donation.payment_method = method.upper()

        if not donation.receipt_number:
            donation.receipt_number = generate_receipt_number()

        donation.paid_at = timezone.now()
        donation.save()

        if not donation.receipt_sent:
            send_receipt_email(donation)

            donation.receipt_sent = True
            donation.save()

    elif status == "FAILED":
        donation.payment_status = "FAILED"
        donation.save()

    return JsonResponse({"status": "ok"})


def get_beneficiary_data():
    token_url = "https://api.khidmattrust.org/api/Account/ValidateKey?Key=KhidmatAPILive"
    data_url = "https://api.khidmattrust.org/api/Display/GetData"

    try:
        token_response = requests.get(token_url, timeout=5)
        token_response.raise_for_status()
        token_data = token_response.json()
        jwt_token = token_data.get("Token") or token_data.get("token")

        if not jwt_token:
            raise ValueError("JWT Token not found in response")

        headers = {"Authorization": f"Bearer {jwt_token}"}
        data_response = requests.get(data_url, headers=headers, timeout=5)
        data_response.raise_for_status()
        api_data = data_response.json()

    except Exception as e:
        print(f"[Third-Party API Error] {e}")
        api_data = {}

    total_medicine = int(api_data.get("Total_Medicine_Application", 0))
    total_hospital = int(api_data.get("Total_Hospitalisation_Application", 0))

    raw_data = BeneficiaryCategory.objects.filter(is_active=True)

    beneficiary_data = {}
    total_beneficiaries = 0

    for item in raw_data:
        key = item.name.strip().replace(" ", "_").lower()

        if item.name == "Medical Aid":
            combined_total = item.number + total_medicine + total_hospital
            beneficiary_data[key] = convert_to_k_format(combined_total)
            total_beneficiaries += total_medicine + total_hospital
        else:
            beneficiary_data[key] = convert_to_k_format(item.number)

        total_beneficiaries += item.number

    beneficiary_data["total_beneficiaries"] = convert_to_k_format(total_beneficiaries)

    return beneficiary_data

def home(request):
    # Step 1: JWT Token API Call
    token_url = "https://api.khidmattrust.org/api/Account/ValidateKey?Key=KhidmatAPILive"
    data_url = "https://api.khidmattrust.org/api/Display/GetData"

    try:
        token_response = requests.get(token_url, timeout=5)  # timeout added
        token_response.raise_for_status()
        token_data = token_response.json()
        jwt_token = token_data.get("Token") or token_data.get("token")

        if not jwt_token:
            raise ValueError("JWT Token not found in response")

        headers = {"Authorization": f"Bearer {jwt_token}"}
        data_response = requests.get(data_url, headers=headers, timeout=5)
        data_response.raise_for_status()
        api_data = data_response.json()
        api_error = False


    except Exception as e:
        print(f"[Third-Party API Error] {e}")
        api_data = {}
        api_error = True
    

    total_medicine = int(api_data.get("Total_Medicine_Application", 0))
    total_hospital = int(api_data.get("Total_Hospitalisation_Application", 0))
    
    raw_data = BeneficiaryCategory.objects.filter(is_active = True).all()

    beneficiary_data = {}
    total_beneficiaries = 0

    for item in raw_data:
        key = item.name.strip().replace(" ", "_").lower()

        if item.name == "Medical Aid":
            table_number = item.number
            combined_total = table_number + total_medicine + total_hospital
            beneficiary_data[key] = convert_to_k_format(combined_total)
            total_beneficiaries += total_medicine + total_hospital
        else:
            beneficiary_data[key] = convert_to_k_format(item.number)
        
        total_beneficiaries += item.number

# Add total beneficiaries
    beneficiary_data["total_beneficiaries"] = convert_to_k_format(total_beneficiaries)
    slider_items = HomeBannerMaster.objects.filter(is_active=True).order_by('order')
    about_section = SystemMaster.objects.filter(system_name='KCT').first()
    casestudy = get_data_dict_casestdy()
    our_vision = SystemMaster.objects.filter(system_name="Our Vision").first()
    our_mission = SystemMaster.objects.filter(system_name="Our Mission").first()
    footer_data = get_footer_data()
    page_quotes = SystemMaster.objects.filter(system_name='quotes', is_active=True)
    logos = PartnerLogo.objects.filter(is_active=True)

    # Final Context
    context = {
        'slider_items': slider_items,
        'about_section': about_section,
        'casestudy': casestudy.items(),
        'our_vision': our_vision,
        'our_mission': our_mission,
        'footer_data': footer_data,
        'page_quotes': page_quotes,
        'logos':logos,
        'beneficiary_data':beneficiary_data
        
    }

    return render(request, 'kct/index.html', context)

def about(request):
    # managinglist = ManagingListCategoryMaster.objects.prefetch_related('items').all()
    managinglist = ManagingListCategoryMaster.objects.filter(is_active=True).prefetch_related('items')
    categories = ListItemCategory.objects.all()  
    about_section_page = get_data_about_page()
    our_aim = SystemMaster.objects.filter(system_name="Our Aim").first()
    our_vision = SystemMaster.objects.filter(system_name="Our Vision").first()
    our_mission = SystemMaster.objects.filter(system_name="Our Mission").first()
    affiliated_trust_category = SystemMasterCategory.objects.filter(name="Affiliated Trust List").first()
    affiliated_trusts = SystemMaster.objects.filter(category=affiliated_trust_category)
    page_quotes = SystemMaster.objects.filter(system_name='quotes', is_active=True)
    afillat = get_data_afillat()
    footer_data = get_footer_data()
    casestudy = get_data_dict_casestdy()
    awards = GalleryItem.objects.filter(is_active=True,category='award_section')
     

    context = {
        'managinglist': managinglist,
        'categories': categories,
        'about_section_page':about_section_page,  
        'our_aim': our_aim,
        'our_vision': our_vision,
        'our_mission': our_mission,
        'affiliated_trusts': afillat,
        'footer_data': footer_data,
        'page_quotes': page_quotes,
        'casestudy':casestudy.items(),
        'awards':awards
        
    }
    return render(request, 'kct/about.html', context)

def activity(request):
    activities_page = get_data_activies()
    gallery_items = get_gallery_images()
    footer_data = get_footer_data()
    page_quotes = SystemMaster.objects.filter(system_name='quotes', is_active=True)
    context = {
        'gallery_items' : gallery_items,
        'activities_page':activities_page,
        'footer_data': footer_data,
        'page_quotes': page_quotes,
    }
    return render(request, 'kct/activities.html', context)

def benefits(request):
    beneficiaryaid = get_data_dict_aid()
    benefits_page = get_data_benefits()
    footer_data = get_footer_data()
    page_quotes = SystemMaster.objects.filter(system_name='quotes', is_active=True)

    context = {
        'beneficiaryaid':beneficiaryaid.items(),
        'benefits_page':benefits_page,
        'footer_data': footer_data,
        'page_quotes': page_quotes,
    }
    return render(request, 'kct/benefits.html',context)

def career(request):
    career_page = get_data_career()
    footer_data = get_footer_data()
    page_quotes = SystemMaster.objects.filter(system_name='quotes', is_active=True)

    context = {
        'career_page':career_page,
        'footer_data': footer_data,
        'page_quotes': page_quotes,
    }
    return render(request, 'kct/careers.html',context)




def contact(request):
    page_quotes = SystemMaster.objects.filter(system_name='quotes', is_active=True)
    footer_data = get_footer_data()
    success = False  

    if request.method == 'POST':
        Name = request.POST.get('name', '').strip()
        Email = request.POST.get('email', '').strip()
        Phone = request.POST.get('phone', '').strip()
        Message = request.POST.get('message', '').strip()


            
        if all([Name, Email, Phone]):
            if KCTEnquireMaster.objects.filter(email=Email).first():
                messages.warning(request, "You have already Sumitted the Form, Please wait we will connect with you within a 24 hours.")
                
            try:
                new_record = KCTEnquireMaster(name=Name, email=Email, phone=Phone, message=Message)
                new_record.save()
                subject = "Thank You for Contacting Us"
                message_body = f"""
                Dear {Name},

                Thank you for reaching out to us. We have received your enquiry and will get back to you soon.

                Your Details:
                Name: {Name}
                Email: {Email}
                Phone: {Phone}
                Message: {Message}

                Best Regards,
                Your Company Name
                """

                print("Waiting")
                form_email = settings.EMAIL_HOST_USER
                recipient_list = ["sadique.leewayzon@gmail.com"]
                send_mail(subject, message_body, form_email, recipient_list)
                messages.success(request, "Your enquiry has been submitted successfully.")

            except Exception as e:
                print(e)
                messages.error(request, f"An error occurred: {str(e)}")

        else:

            messages.error(request, "Please fill in all required fields.")

        print(Name, Email, Phone, Message)

        

    context = {
        'footer_data': footer_data,
        'page_quotes': page_quotes,
    }
    return render(request, 'kct/contact.html',context)





# def donate(request):
#     donate_data = SystemMaster.objects.get(system_name="Donate Section")
#     footer_data = get_footer_data()
#     if request.method == "POST":
#         amount = request.POST.get('amount')

#         amount_in_paise = int(float(amount))

#         client = razorpay.Client(auth=('rzp_test_xiMcTjBlVV2j8h', 'AREBxhesXkY9EsfTJjAJT5AD'))
        
#         order = client.order.create({
#             'amount': amount_in_paise,  
#             'currency': 'INR',
#             'payment_capture': '1'  
#         })

#         return JsonResponse(order) 
    

#     context = {
#         'donate_data':donate_data,
#         'footer_data': footer_data,
#     }
#     return render(request, 'kct/donate.html',context)




# client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))
def donate(request):
    donate_data = SystemMaster.objects.get(system_name="Donate Section")
    footer_data = get_footer_data()
    beneficiary_data = get_beneficiary_data()
    


    context = {
        'donate_data': donate_data,
        'footer_data': footer_data,
        'beneficiary_data': beneficiary_data,
        # 'form': form,
    }
    return render(request, 'kct/donate.html', context)




# @csrf_exempt
# def payment_success(request):
#     if request.method == 'POST':
#         print("Payment success view called!")  

#         try:
            
#             data = json.loads(request.body)
#             payment_id = data.get('razorpay_payment_id')
#             order_id = data.get('razorpay_order_id')
#             signature = data.get('razorpay_signature')

#             print(f"Payment ID: {payment_id}, Order ID: {order_id}, Signature: {signature}")  
#             params_dict = {
#                 'razorpay_order_id': order_id,
#                 'razorpay_payment_id': payment_id,
#                 'razorpay_signature': signature,
#             }

#             client.utility.verify_payment_signature(params_dict)
#             print("Signature verification successful!")  

#             donation = Donation.objects.get(razorpay_order_id=order_id)
#             donation.payment_status = 'COMPLETED'
#             donation.save()
#             print("Payment status updated to COMPLETED!")  

#             return JsonResponse({'status': 'success'})
#         except Exception as e:
#             print(f"Error: {e}")  
#             return JsonResponse({'status': 'failure', 'error': str(e)})
#     return JsonResponse({'error': 'Invalid request'}, status=400)






def dialysis(request):
    footer_data = get_footer_data()

    context = {
        'footer_data': footer_data,
    }
    return render(request, 'kct/event-dialysis-centre.html',context)



def ramzan(request):
    footer_data = get_footer_data()

    context = {
        'footer_data': footer_data,
    }
    return render(request, 'kct/event-ramzan-and-monthly-ration-aid.html',context)




def help(request):
    footer_data = get_footer_data()

    context = {
        'footer_data': footer_data,
    }
    return render(request, 'kct/event-why-should-anyone-approach-kct-for-help-and-assistance.html',context)


def event_detail(request, slug):
    event = get_object_or_404(SystemMaster, system_title__icontains=slug)
    return render(request, 'event_detail.html', {'event': event})


def displayParticularEvent(request, eventId):
    eventDetail = EventMaster.objects.filter(id=eventId, is_active=True).order_by('order')
    everEvent = EventMaster.objects.exclude(id=eventId)
    eventQuote = EventMaster.objects.filter(id=eventId, is_active=True)
    footer_data = get_footer_data()

    context = {
        'eventDetail': eventDetail,
        'everEvent': everEvent,
        'eventQuote':eventQuote,
        'footer_data': footer_data
        
        }
    return render(request, 'kct/event-dialysis-centre.html', context)

def govtScheme(request, schemeId):
    govtscheme = GovtSchemeMaster.objects.filter(id=schemeId, is_active=True).order_by('order')
    govtschemes = GovtSchemeMaster.objects.exclude(id=schemeId)
    
    footer_data = get_footer_data()

    context = {
        'govtscheme': govtscheme,
        'govtschemes': govtschemes,
        'footer_data': footer_data
        
        }
    return render(request, 'kct/govt-scheme.html', context)


def projectDetail(request, projectId):
    project_detail = ProjectMaster.objects.filter(id=projectId, is_active=True).order_by('order')
    project_details = ProjectMaster.objects.exclude(id=projectId)
    project_imgs = ProjectImage.objects.filter(project__id=projectId, is_active=True)
    print(project_imgs)
    
    footer_data = get_footer_data()

    context = {
        'project_detail': project_detail,
        'project_details': project_details,
        'footer_data': footer_data,
        'project_imgs':project_imgs
        
        }
    return render(request, 'kct/project-details.html', context)

def news(request):
     footer_data = get_footer_data()
     kct_news = GalleryItem.objects.filter(is_active=True,category='news_section')
     context = {
        'footer_data': footer_data,
        'kct_news':kct_news
        }
     return render(request, "kct/news.html",context)


def anual_report(request):
     footer_data = get_footer_data()
     context = {
        'footer_data': footer_data
        }
     return render(request, "kct/anual_report.html",context)

def gallery(request):
    gallery_items = GalleryItem.objects.filter(is_active=True,category='gallery_page')
    footer_data = get_footer_data()
    context = {
        'footer_data': footer_data,
        'gallery_items': gallery_items
        }
    return render(request, "kct/gallery.html",context)

def success_story(request):
    footer_data = get_footer_data()
    context = {
        'footer_data': footer_data
        }
    return render(request, "kct/success_story.html",context)


def donation_terms(request):
    """Donation Terms & Conditions page"""
    footer_data = get_footer_data()
    term_and_condition= get_data_dict_term_and_condition()
    
    context = {
        'footer_data': footer_data,
        'term_and_condition':term_and_condition.items()
 
    }
    return render(request, 'kct/donation_terms.html', context)

def payment_success(request):
    order_id = request.GET.get("order_id")
    donation = Donation.objects.filter(order_id=order_id).first()
    return render(request, "kct/payment_success.html", {"donation": donation})