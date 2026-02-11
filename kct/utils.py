from kct.models import Donation, SystemMaster
import os
from django.template.loader import render_to_string
from weasyprint import HTML
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils.timezone import now
from django.db.models import Max
from io import BytesIO
 
def get_data_dict():
    try:
        key_record = SystemMaster.objects.get(system_name="Key Programs")
        
        titles = [title.strip() for title in key_record.system_title.split("^")]
        descriptions = [desc.strip() for desc in key_record.system_value.split("\n") if desc.strip()]
        
        if len(titles) != len(descriptions):
            raise ValueError("Mismatch between number of titles and descriptions.")
        
        data_dict = {title: description for title, description in zip(titles, descriptions)}
        
        return data_dict
    
    except SystemMaster.DoesNotExist:
        print("Key Programs record does not exist.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    


def get_data_dict_aid():
    try:
        beneficiaries_aid_record = SystemMaster.objects.get(system_name="BENEFICIARIES AID")
        
        titles = [title.strip() for title in beneficiaries_aid_record.system_title.split("^")]
        descriptions = [desc.strip() for desc in beneficiaries_aid_record.system_value.split("\n") if desc.strip()]
        
        if len(titles) != len(descriptions):
            raise ValueError("Mismatch between number of titles and descriptions.")
        
        data_dict = {title: description for title, description in zip(titles, descriptions)}
        
        return data_dict
    
    except SystemMaster.DoesNotExist:
        print("BENEFICIARIES AID record does not exist.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    
def get_data_dict_casestdy():
    try:
        case_study_record = SystemMaster.objects.get(system_name="Case Studies")
        # Split the system titles and values
        titles = [title.strip() for title in case_study_record.system_title.split("^")]
        descriptions = [desc.strip() for desc in case_study_record.system_value.split("\n") if desc.strip()]
        
        # Map each title to its corresponding description
        data_dict = {title: description for title, description in zip(titles, descriptions)}
        
        return data_dict
    
    except SystemMaster.DoesNotExist:
        print("Case Studies record does not exist.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    
def get_data_dict_Event():
    try:
        latest_event_record = SystemMaster.objects.get(system_name="Our Latest Event")
        
        # Split the system titles and values
        titles = [title.strip() for title in latest_event_record.system_title.split("^")]
        descriptions = [desc.strip() for desc in latest_event_record.system_value.split("\n") if desc.strip()]

        # Map each title to its corresponding description
        data_dict = {title: description for title, description in zip(titles, descriptions)}
        
        return data_dict
    
    except SystemMaster.DoesNotExist:
        print("Latest Event record does not exist.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    

def get_gallery_images():
    try:
        gallery_records = SystemMaster.objects.filter(system_name="Gallery").order_by('created_at')
        # print(gallery_records, "gallery_records**********************************")

        return gallery_records

    except SystemMaster.DoesNotExist:
        print("Gallery records do not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

from kct.models import SystemMaster

 
def get_data_about_page():
    try:
        about_page_record = SystemMaster.objects.get(system_name="about page Programs")

        title = about_page_record.system_title.strip() if about_page_record.system_title else "About Us"
        descriptions = [desc.strip() for desc in about_page_record.system_value.split("\n") if desc.strip()]  # Split into paragraphs

        return {'title': title, 'descriptions': descriptions}  

    except SystemMaster.DoesNotExist:
        print("about page record does not exist.")
        return {'title': "About Us", 'descriptions': []}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'title': "About Us", 'descriptions': []}


def get_data_activies():
    try:
        get_data_activies = SystemMaster.objects.get(system_name="activities page")

        title = get_data_activies.system_title.strip() if get_data_activies.system_title else "About Us"
        descriptions = get_data_activies.system_value.strip() if get_data_activies.system_value else ""

        return {'title': title, 'descriptions': descriptions}  

    except SystemMaster.DoesNotExist:
        print("get_data_activies record does not exist.")
        return {'title': "About Us", 'descriptions': []}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'title': "About Us", 'descriptions': []}
    

def get_data_benefits():
    try:
        get_data_benefits = SystemMaster.objects.get(system_name="benefits page")

        title = get_data_benefits.system_title.strip() if get_data_benefits.system_title else "About Us"
        descriptions = get_data_benefits.system_value.strip() if get_data_benefits.system_value else ""

        return {'title': title, 'descriptions': descriptions}  

    except SystemMaster.DoesNotExist:
        print("get_data_benefits record does not exist.")
        return {'title': "About Us", 'descriptions': []}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'title': "About Us", 'descriptions': []}
    
def get_data_career():
    try:
        get_data_career = SystemMaster.objects.get(system_name="career page")

        title = get_data_career.system_title.strip() if get_data_career.system_title else "About Us"
        descriptions = get_data_career.system_value.strip() if get_data_career.system_value else ""

        return {'title': title, 'descriptions': descriptions}  

    except SystemMaster.DoesNotExist:
        print("get_data_career record does not exist.")
        return {'title': "About Us", 'descriptions': []}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'title': "About Us", 'descriptions': []}
    


def get_data_afillat():
    try:
        affiliate_record = SystemMaster.objects.get(system_name='Afillated')
        data_str = affiliate_record.system_value
        each_data = [item.strip() for item in data_str.split(',')]
        return each_data 
    except SystemMaster.DoesNotExist:
        return []


def get_footer_data():
    try:
        # Fetch the footer record
        footer_record = SystemMaster.objects.get(system_name="footer")
        
        # Splitting the titles and descriptions while removing empty values
        titles = [title.strip() for title in footer_record.system_title.split("^") if title.strip()]
        descriptions = [desc.strip() for desc in footer_record.system_value.split("\r\n\r\n") if desc.strip()]  
        # Using "\r\n\r\n" as a separator to properly split sections
        
        # Ensure titles and descriptions match correctly
        footer_data = {}
        for i, title in enumerate(titles):
            footer_data[title] = descriptions[i] if i < len(descriptions) else ""

        # Debugging output to check accuracy
        # print("Extracted Footer Data:", footer_data)

        return footer_data

    except SystemMaster.DoesNotExist:
        print("Footer record does not exist.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}



def convert_to_k_format(number):
    if number >= 1000:
        return f"{round(number / 1000, 1)}K+"
    return str(number)


def get_data_dict_term_and_condition():
    try:
        term_and_condition = SystemMaster.objects.get(system_name="term_and_condition")
        # Split the system titles and values
        titles = [title.strip() for title in term_and_condition.system_title.split("^")]
        descriptions = [desc.strip() for desc in term_and_condition.system_value.split("\n") if desc.strip()]
        
        # Map each title to its corresponding description
        data_dict = {title: description for title, description in zip(titles, descriptions)}
        
        return data_dict
    
    except SystemMaster.DoesNotExist:
        print("Term and Condition record does not exist.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    

def send_receipt_email(donation):
    # Render HTML template
    html = render_to_string(
        "kct/receipts/receipt.html",
        {"donation": donation}
    )

    # Generate PDF in memory
    pdf_buffer = BytesIO()
    HTML(string=html).write_pdf(pdf_buffer)
    pdf_buffer.seek(0)

    subject = "Donation Receipt – Khidmat Charitable Trust"

    body = f"""
Dear {donation.name},

Thank you for your generous donation of ₹{donation.amount}.

Please find your receipt attached.
This receipt is valid for 80G tax exemption.

Order ID: {donation.order_id}

Regards,
Khidmat Charitable Trust
"""

    email = EmailMessage(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [donation.email],
    )

    # Attach PDF directly (no file path)
    email.attach(
        f"receipt_{donation.order_id}.pdf",
        pdf_buffer.read(),
        "application/pdf"
    )

    email.send()


def generate_receipt_number():
    year = now().year

    last_receipt = Donation.objects.filter(
        receipt_number__startswith=f"KCT-{year}-"
    ).aggregate(Max("receipt_number"))

    if last_receipt["receipt_number__max"]:
        last_number = int(
            last_receipt["receipt_number__max"].split("-")[-1]
        )
        new_number = last_number + 1
    else:
        new_number = 1

    return f"KCT-{year}-{str(new_number).zfill(4)}"