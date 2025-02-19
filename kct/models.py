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
        null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.system_name if self.system_name else "System Master Entry"


class EventMaster(models.Model):
    event_title = models.CharField(max_length=255)
    event_description = models.TextField()
    event_feature = models.TextField(max_length=10000, blank=True)
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
    is_active = models.BooleanField(default=True)
 

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class KeyProgramMaster(models.Model):
    system = models.OneToOneField(SystemMaster, on_delete=models.CASCADE, related_name="key_program_master")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.system.system_name


class BeneficiaryAid(models.Model):
    system = models.OneToOneField(SystemMaster, on_delete=models.CASCADE, related_name="beneficiary_aid")
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.system.system_name


class CaseStudiesMaster(models.Model):
    system = models.OneToOneField(SystemMaster, on_delete=models.CASCADE, related_name="case_study_master")
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.system.system_name


class LatestEventMaster(models.Model):
    system = models.OneToOneField(SystemMaster, on_delete=models.CASCADE, related_name="latest_event_master")
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.system.system_name


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