from django.contrib import admin
from import_export import resources 
from .models import SystemMaster, BeneficiaryCategory, ManagingListCategoryMaster, ListItemCategory, DropdownOption, EventMaster
from import_export.admin import ImportExportModelAdmin


class SystemMasterresources(resources.ModelResource):
    class Meta:
        model = SystemMaster
        import_id_fields = ['id']
        fields = ['id', 'category', 'system_name', 'system_title', 'system_value','is_active']


class SystemMasterAdmin(ImportExportModelAdmin):
    resource_class = SystemMasterresources
    list_display = [field.name for field in SystemMaster._meta.get_fields()]
    search_fields = ['id','system_name', 'system_title']

admin.site.register(SystemMaster,SystemMasterAdmin)



class EventMasterresources(resources.ModelResource):
    class Meta:
        model = EventMaster
        import_id_fields = ['id'] 
        fields = ['id', 'event_title', 'event_description', 'is_active']  
class EventMasterAdmin(ImportExportModelAdmin):
    # list_display = ('event_title','event_description','is_active')
    resource_class = EventMasterresources
    list_display = [field.name for field in EventMaster._meta.get_fields()]
    search_fields = ['id','event_title']

admin.site.register(EventMaster,EventMasterAdmin)







class BeneficiaryCategoryresources(resources.ModelResource):
    class Meta:
        model = BeneficiaryCategory
        import_id_fields = ['id'] 
        fields = ['id', 'name', 'number', 'is_active']  
class BeneficiaryCategoryAdmin(ImportExportModelAdmin):
    resource_class = BeneficiaryCategoryresources
    list_display = ['id', 'name', 'number', 'is_active']
    search_fields = ['id','name']

admin.site.register(BeneficiaryCategory,BeneficiaryCategoryAdmin)  


  



class ManagingList(resources.ModelResource):
    class Meta:
        model = ManagingListCategoryMaster
        import_id_fields = ['id']
        fields = ['id', 'title', 'is_active']
        
class ManagingListAdmin(ImportExportModelAdmin):
    resource_class = ManagingList
    list_display = ['id', 'title', 'is_active']
    search_fields = ['id', 'title']


admin.site.register(ManagingListCategoryMaster, ManagingListAdmin)  





class ListItem(resources.ModelResource):
    class Meta:
        model = ListItemCategory
        import_id_fields = ['id']
        fields = ['name', 'is_active']


class ListItemAdmin(ImportExportModelAdmin):
    resource_class = ListItem
    list_display = ['id', 'name', 'is_active']
    search_fields = ['id', 'name']


admin.site.register(ListItemCategory, ListItemAdmin) 
 

class dropdownoptions(resources.ModelResource):
    class Meta:
        model = DropdownOption
        import_id_fields = ['id']
        fields = ['category', 'name', 'is_active']

class dropdownoptionsAdmin(ImportExportModelAdmin):
    resource_class = dropdownoptions
    list_display = ['id','category', 'name', 'is_active']
    search_fields = ['id', 'name']
admin.site.register(DropdownOption, dropdownoptionsAdmin)

