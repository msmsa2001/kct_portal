from django.contrib import admin
from import_export import resources 
from .models import  GalleryItem, GovtSchemeMaster, HomeBannerMaster, KCTEnquireMaster, PartnerLogo, ProjectImage, ProjectMaster, SystemMaster, BeneficiaryCategory, ManagingListCategoryMaster, ListItemCategory, DropdownOption, EventMaster, BeneficiaryData
from import_export.admin import ImportExportModelAdmin



admin.site.site_header = "Khidmat Charitable Trust Admin Panel"
admin.site.site_title = "KCT Admin Portal"
admin.site.index_title = "Welcome to Khidmat Charitable Trust Dashboard"


class SystemMasterresources(resources.ModelResource):
    class Meta:
        model = SystemMaster
        import_id_fields = ['id']
        fields = ['id', 'category', 'system_name', 'system_title', 'system_value', 'system_img', 'is_active']

class SystemMasterAdmin(ImportExportModelAdmin):
    resource_class = SystemMasterresources
    list_display = ['id', 'category', 'system_name', 'system_title','system_img', 'is_active']
    search_fields = ['id','system_name', 'system_title']

admin.site.register(SystemMaster,SystemMasterAdmin)


class KCTEnquireMasterresource(resources.ModelResource):
    class Meta:
        model = KCTEnquireMaster
        import_id_fields = ['id']
        fields = ['id', 'name', 'email', 'phone', 'message', 'is_active']

class KCTEnquireMasterAdmin(ImportExportModelAdmin):
    resource_class = KCTEnquireMasterresource
    list_display = ['id','name', 'email', 'phone', 'message', 'is_active']
    search_fields = ['id', 'name', 'email', 'phone']
admin.site.register(KCTEnquireMaster, KCTEnquireMasterAdmin)



class ProjectMasterresources(resources.ModelResource):
    class Meta:
        model = ProjectMaster
        import_id_fields = ['id'] 
        # fields = ['id', 'event_title', 'event_description','event_feature', 'event_img', 'reactions', 'time', 'order', 'is_active']  
class ProjectMasterAdmin(ImportExportModelAdmin):
    list_display = ('project_title','project_description','time','order','is_active')
    list_editable = ('order',)
    resource_class = ProjectMasterresources
    search_fields = ['id',]

admin.site.register(ProjectMaster,ProjectMasterAdmin)



class HomeBannerMasterresources(resources.ModelResource):
    class Meta:
        model = HomeBannerMaster
        import_id_fields = ['id'] 
        # fields = ['id', 'event_title', 'event_description','event_feature', 'event_img', 'reactions', 'time', 'order', 'is_active']  
class HomeBannerMasterAdmin(ImportExportModelAdmin):
    # list_display = ('event_title','event_description','is_active')
    resource_class = HomeBannerMasterresources
    list_display = [field.name for field in HomeBannerMaster._meta.get_fields()]
    list_editable = ('order',)
    search_fields = ['id','event_title']

admin.site.register(HomeBannerMaster,HomeBannerMasterAdmin)


class ProjectImageresources(resources.ModelResource):
    class Meta:
        model = ProjectImage
        import_id_fields = ['id'] 
        # fields = ['id', 'event_title', 'event_description','event_feature', 'event_img', 'reactions', 'time', 'order', 'is_active']  
class ProjectImageAdmin(ImportExportModelAdmin):
    # list_display = ('event_title','event_description','is_active')
    resource_class = ProjectImageresources
    list_display = [field.name for field in ProjectImage._meta.get_fields()]
    search_fields = ['id',]

admin.site.register(ProjectImage,ProjectImageAdmin)



class PartnerLogoresources(resources.ModelResource):
    class Meta:
        model = PartnerLogo
        import_id_fields = ['id'] 
class PartnerLogoAdmin(ImportExportModelAdmin):
    resource_class = PartnerLogoresources
    list_display = [field.name for field in PartnerLogo._meta.get_fields()]
    search_fields = ['id',]

admin.site.register(PartnerLogo,PartnerLogoAdmin)



class GalleryItemresources(resources.ModelResource):
    class Meta:
        model = GalleryItem
        import_id_fields = ['id'] 
class GalleryItemAdmin(ImportExportModelAdmin):
    resource_class = GalleryItemresources
    list_display = [field.name for field in GalleryItem._meta.get_fields()]
    search_fields = ['id',]

admin.site.register(GalleryItem,GalleryItemAdmin)


class BeneficiaryCategoryresources(resources.ModelResource):
    class Meta:
        model = BeneficiaryCategory
        import_id_fields = ['id'] 
        fields = ['id', 'name', 'icon', 'number', 'has_dropdown', 'is_active']  
class BeneficiaryCategoryAdmin(ImportExportModelAdmin):
    resource_class = BeneficiaryCategoryresources
    list_display = ['id', 'name', 'number', 'is_active']
    search_fields = ['id','name']

admin.site.register(BeneficiaryCategory,BeneficiaryCategoryAdmin)
