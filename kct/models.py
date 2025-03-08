from django.db import models
from django.core.validators import FileExtensionValidator

class SystemMasterCategory(models.Model):
    name = models.CharField(max_length=255, unique=True) 

    def __str__(self):
        return self.name

class SystemMaster(models.Model):
    category = models.ForeignKey(SystemMasterCategory, on_delete=models.CASCADE, null=True, blank=True)
    system_name = models.CharField(max_length=255, null=True)
    system_title = models.TextField(null=True, blank=True)
    system_value = models.TextField(null=True, blank=True)
    system_img = models.FileField(
        upload_to='banner/', 
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp', 'svg'])], 
        null=True, blank=True)
    page_quotes = models.TextField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.system_name if self.system_name else "System Master Entry"



# Data inserts from Django panel in this model.
class EventMaster(models.Model):
    event_title = models.CharField(max_length=255)
    event_description = models.TextField()
    event_feature = models.TextField(max_length=10000, blank=True)
    event_quotes = models.TextField(max_length=255, blank=True)
    event_img = models.FileField(upload_to='event_images/')
    reactions = models.PositiveIntegerField(default=0)
    time = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.event_title
    




class BeneficiaryCategory(models.Model):
    name = models.CharField(max_length=100, default='Default Name')  
    icon = models.FileField(upload_to='icons/', null=True, blank=True)
    number = models.PositiveIntegerField(default=0)  
    has_dropdown = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name


class DropdownOption(models.Model):
    category = models.ForeignKey(
        BeneficiaryCategory,
        on_delete=models.CASCADE,
        related_name="dropdown_options"
    )
    name = models.CharField(max_length=100)
    count = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
 

    def __str__(self):
        return f"{self.name} ({self.category.name})"



class ManagingListCategoryMaster(models.Model):
    title = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title


class ListItemCategory(models.Model):
    category = models.ForeignKey(ManagingListCategoryMaster, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} -> {self.category.title}"
    

class KCTEnquireMaster(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name} {self.email} {self.phone}"
    





# class Donation(models.Model):
    # PAYMENT_CHOICES = [
    #     ('personal-account', 'Personal Account'),
    #     ('official-account', 'Official Account'),
    # ]
    # PURPOSE_CHOICES = [
    #     ('zakat', 'Zakat'),
    #     ('fi-sabilillah', 'Fi Sabilillah'),
    #     ('sadqa', 'Sadqa'),
    #     ('interest', 'Interest'),
    #     ('others', 'Others'),
    # ]

    # whypay = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    # paying_from = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    # amount = models.DecimalField(max_digits=15, decimal_places=2)

    # # Personal Account Fields
    # fullname = models.CharField(max_length=255, blank=True, null=True)
    # phone = models.CharField(max_length=15, blank=True, null=True)
    # email = models.EmailField(blank=True, null=True)
    # pan = models.CharField(max_length=20, blank=True, null=True)
    # aadhar = models.CharField(max_length=20, blank=True, null=True)
    # address = models.TextField(blank=True, null=True)

    # # Official Account Fields
    # company_name = models.CharField(max_length=255, blank=True, null=True)
    # company_phone = models.CharField(max_length=15, blank=True, null=True)
    # company_address = models.TextField(blank=True, null=True)
    # company_email = models.EmailField(blank=True, null=True)
    # company_pan = models.CharField(max_length=20, blank=True, null=True)
    # contact_person_name = models.CharField(max_length=255, blank=True, null=True)
    # contact_person_phone = models.CharField(max_length=15, blank=True, null=True)
    # PAYMENT_STATUS_CHOICES = [
    #     ('PENDING', 'Pending'),
    #     ('COMPLETED', 'Completed'),
    #     ('FAILED', 'Failed'),
    # ]
    # payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='PENDING')
    # razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)

    # created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.system.system_name