from django.contrib import admin
from import_export import resources 
from .models import  GalleryItem, GovtSchemeMaster, HomeBannerMaster, KCTEnquireMaster, PartnerLogo, ProjectImage, ProjectMaster, SystemMaster, BeneficiaryCategory, ManagingListCategoryMaster, ListItemCategory, DropdownOption, EventMaster, BeneficiaryData
from import_export.admin import ImportExportModelAdmin




# class SystemMasterCategoryresources(resources.ModelResource):
#     class Meta:
#         model = SystemMasterCategory
#         import_id_fields = ['id']
#         fields = ['id', 'name']


# class SystemMasterCategoryAdmin(ImportExportModelAdmin):
#     resource_class = SystemMasterCategoryresources
#     list_display = ['id', 'name']
#     search_fields = ['id','name']

# admin.site.register(SystemMasterCategory,SystemMasterCategoryAdmin)



class SystemMasterresources(resources.ModelResource):
    class Meta:
        model = SystemMaster
        import_id_fields = ['id']
        fields = ['id', 'category', 'system_name', 'system_title', 'system_value', 'system_img', 'is_active']


class SystemMasterAdmin(ImportExportModelAdmin):
    resource_class = SystemMasterresources
    list_display = [field.name for field in SystemMaster._meta.get_fields()]
    search_fields = ['id','system_name', 'system_title']

admin.site.register(SystemMaster,SystemMasterAdmin)



class EventMasterresources(resources.ModelResource):
    class Meta:
        model = EventMaster
        import_id_fields = ['id'] 
        fields = ['id', 'event_title', 'event_description','event_feature', 'event_img', 'reactions', 'time', 'order', 'is_active']  
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
        fields = ['id', 'name', 'icon', 'number', 'has_dropdown', 'is_active']  
class BeneficiaryCategoryAdmin(ImportExportModelAdmin):
    resource_class = BeneficiaryCategoryresources
    list_display = ['id', 'name', 'number', 'is_active']
    search_fields = ['id','name']

admin.site.register(BeneficiaryCategory,BeneficiaryCategoryAdmin)  
 


 

class dropdownoptions(resources.ModelResource):
    class Meta:
        model = DropdownOption
        import_id_fields = ['id']
        fields = ['id','category', 'name', 'is_active']

class dropdownoptionsAdmin(ImportExportModelAdmin):
    resource_class = dropdownoptions
    list_display = ['id','category', 'name', 'count','is_active']
    search_fields = ['id', 'name']
admin.site.register(DropdownOption, dropdownoptionsAdmin)




# class KeyProgramMasterresource(resources.ModelResource):
#     class Meta:
#         model = KeyProgramMaster
#         import_id_fields = ['id']
#         fields = ['id','system', 'is_active']

# class KeyProgramMasterAdmin(ImportExportModelAdmin):
#     resource_class = KeyProgramMasterresource
#     list_display = ['id','system', 'is_active']
#     search_fields = ['id', 'name']
# admin.site.register(KeyProgramMaster, KeyProgramMasterAdmin)




# class BeneficiaryAidresource(resources.ModelResource):
#     class Meta:
#         model = BeneficiaryAid
#         import_id_fields = ['id']
#         fields = ['id', 'system', 'is_active']

# class BeneficiaryAidAdmin(ImportExportModelAdmin):
#     resource_class = BeneficiaryAidresource
#     list_display = ['id','system', 'is_active']
#     search_fields = ['id', 'name']
# admin.site.register(BeneficiaryAid, BeneficiaryAidAdmin)



# class CaseStudiesMasterresource(resources.ModelResource):
#     class Meta:
#         model = CaseStudiesMaster
#         import_id_fields = ['id']
#         fields = ['id', 'system', 'is_active']

# class CaseStudiesMasterAdmin(ImportExportModelAdmin):
#     resource_class = CaseStudiesMasterresource
#     list_display = ['id','system', 'is_active']
#     search_fields = ['id', 'name']
# admin.site.register(CaseStudiesMaster, CaseStudiesMasterAdmin)






# class LatestEventMasterresource(resources.ModelResource):
#     class Meta:
#         model = LatestEventMaster
#         import_id_fields = ['id']
#         fields = ['id', 'system', 'is_active']

# class LatestEventMasterAdmin(ImportExportModelAdmin):
#     resource_class = LatestEventMasterresource
#     list_display = ['id','system', 'is_active']
#     search_fields = ['id', 'name']
# admin.site.register(LatestEventMaster, LatestEventMasterAdmin)





class ManagingListCategoryresources(resources.ModelResource):
    class Meta:
        model = ManagingListCategoryMaster
        import_id_fields = ['id']
        fields = ['id', 'title', 'is_active']
        
class ManagingListCategoryAdmin(ImportExportModelAdmin):
    resource_class = ManagingListCategoryresources
    list_display = ['id', 'title', 'is_active']
    search_fields = ['id', 'title']


admin.site.register(ManagingListCategoryMaster, ManagingListCategoryAdmin) 







class ListItem(resources.ModelResource):
    class Meta:
        model = ListItemCategory
        import_id_fields = ['id']
        fields = ['id', 'category', 'name' 'is_active']


class ListItemAdmin(ImportExportModelAdmin):
    resource_class = ListItem
    list_display = ['id', 'name', 'is_active']
    search_fields = ['id', 'name']


admin.site.register(ListItemCategory, ListItemAdmin) 





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
    # list_display = ('event_title','event_description','is_active')
    resource_class = ProjectMasterresources
    list_display = [
    field.name for field in ProjectMaster._meta.get_fields()
    if not (field.one_to_many or field.many_to_many)
]
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
    search_fields = ['id','event_title']

admin.site.register(HomeBannerMaster,HomeBannerMasterAdmin)



class GovtSchemeMasterresources(resources.ModelResource):
    class Meta:
        model = GovtSchemeMaster
        import_id_fields = ['id'] 
        # fields = ['id', 'event_title', 'event_description','event_feature', 'event_img', 'reactions', 'time', 'order', 'is_active']  
class GovtSchemeMasterAdmin(ImportExportModelAdmin):
    # list_display = ('event_title','event_description','is_active')
    resource_class = GovtSchemeMasterresources
    list_display = [field.name for field in GovtSchemeMaster._meta.get_fields()]
    search_fields = ['id','event_title']

admin.site.register(GovtSchemeMaster,GovtSchemeMasterAdmin)



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




class BeneficiaryDataresources(resources.ModelResource):
    class Meta:
        model = BeneficiaryData
        import_id_fields = ['id'] 
class BeneficiaryDataAdmin(ImportExportModelAdmin):
    resource_class = BeneficiaryDataresources
    list_display = [field.name for field in BeneficiaryData._meta.get_fields()]
    search_fields = ['id',]

admin.site.register(BeneficiaryData,BeneficiaryDataAdmin)




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
