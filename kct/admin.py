from django.contrib import admin
from .models import SystemMaster, BeneficiaryCategory, ManagingListCategoryMaster, ListItemCategory, DropdownOption

admin.site.register(SystemMaster)  
admin.site.register(BeneficiaryCategory)  
admin.site.register(ManagingListCategoryMaster)  
admin.site.register(ListItemCategory)  
admin.site.register(DropdownOption)
