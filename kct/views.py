from django.shortcuts import render

from kct_portal import settings
from .models import KCTEnquireMaster, SystemMaster,SystemMasterCategory, BeneficiaryCategory, ManagingListCategoryMaster, ListItemCategory, BeneficiaryCategory
from .utils import get_data_afillat, get_data_dict, get_data_dict_aid, get_data_dict_casestdy, get_data_dict_Event, get_gallery_images, get_data_about_page, get_data_activies,get_data_benefits, get_data_career, get_footer_data
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse

def home(request):
    master_items = SystemMaster.objects.all()  
    about_section = SystemMaster.objects.filter(system_name='KCT').first()
    categories = BeneficiaryCategory.objects.prefetch_related('dropdown_options').all()
    key_program_data = get_data_dict()
    beneficiaryaid = get_data_dict_aid()
    casestudy = get_data_dict_casestdy()
    latestevent = get_data_dict_Event()
    our_aim = SystemMaster.objects.filter(system_name="Our Aim").first()
    our_vision = SystemMaster.objects.filter(system_name="Our Vision").first()
    our_mission = SystemMaster.objects.filter(system_name="Our Mission").first()
    footer_data = get_footer_data()
     

    context = {
        'master_items': master_items,  
        'about_section': about_section,
        'categories': categories,  
        'keyprogram': key_program_data.items(),
        'beneficiaryaid':beneficiaryaid.items(),
        'casestudy':casestudy.items(),
        'latestevent':latestevent.items(),
        'our_aim': our_aim,
        'our_vision': our_vision,
        'our_mission': our_mission,
        'footer_data': footer_data,
        
    }
    return render(request, 'kct/index.html', context)

def about(request):
    managinglist = ManagingListCategoryMaster.objects.prefetch_related('items').all()
    categories = ListItemCategory.objects.all()  
    about_section_page = get_data_about_page()
    our_aim = SystemMaster.objects.filter(system_name="Our Aim").first()
    our_vision = SystemMaster.objects.filter(system_name="Our Vision").first()
    our_mission = SystemMaster.objects.filter(system_name="Our Mission").first()
    affiliated_trust_category = SystemMasterCategory.objects.filter(name="Affiliated Trust List").first()
    affiliated_trusts = SystemMaster.objects.filter(category=affiliated_trust_category)
    afillat = get_data_afillat()
    footer_data = get_footer_data()
     

    context = {
        'managinglist': managinglist,
        'categories': categories,
        'about_section_page':about_section_page,  
        'our_aim': our_aim,
        'our_vision': our_vision,
        'our_mission': our_mission,
        'affiliated_trusts': afillat,
        'footer_data': footer_data,
        
    }
    return render(request, 'kct/about.html', context)

def activity(request):
    activities_page = get_data_activies()
    gallery_items = get_gallery_images()
    footer_data = get_footer_data()
    context = {
        'gallery_items' : gallery_items,
        'activities_page':activities_page,
        'footer_data': footer_data,
    }
    return render(request, 'kct/activities.html', context)

def benefits(request):
    beneficiaryaid = get_data_dict_aid()
    benefits_page = get_data_benefits()
    footer_data = get_footer_data()

    context = {
        'beneficiaryaid':beneficiaryaid.items(),
        'benefits_page':benefits_page,
        'footer_data': footer_data,
    }
    return render(request, 'kct/benefits.html',context)

def career(request):
    career_page = get_data_career()
    footer_data = get_footer_data()

    context = {
        'career_page':career_page,
        'footer_data': footer_data,
    }
    return render(request, 'kct/careers.html',context)




def contact(request):
    footer_data = get_footer_data()
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
                form_email = settings.EMAIL_HOST_USER
                recipient_list = [Email]
                send_mail(subject, message_body, form_email, recipient_list)
                messages.success(request, "Your enquiry has been submitted successfully.")

            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")

        else:
            messages.error(request, "Please fill in all required fields.")

        print(Name, Email, Phone, Message)

    context = {
        'footer_data': footer_data,
    }
    return render(request, 'kct/contact.html',context)





def donate(request):
    donate_data = SystemMaster.objects.get(system_name="Donate Section")
    footer_data = get_footer_data()
    if request.method == "POST":
        amount = request.POST.get('amount')

        # Convert amount to paise (Razorpay expects amount in the smallest currency unit)
        amount_in_paise = int(float(amount))

        # Initialize Razorpay client
        client = razorpay.Client(auth=('rzp_test_xiMcTjBlVV2j8h', 'AREBxhesXkY9EsfTJjAJT5AD'))
        
        # Create Razorpay order
        order = client.order.create({
            'amount': amount_in_paise,  # Amount in paise
            'currency': 'INR',
            'payment_capture': '1'  # Auto-capture payment
        })

        return JsonResponse(order) 
    

    context = {
        'donate_data':donate_data,
        'footer_data': footer_data,
    }
    return render(request, 'kct/donate.html',context)





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

