from django.contrib import admin
from import_export import resources 
from .models import  Donation, GalleryItem, GovtSchemeMaster, HomeBannerMaster, KCTEnquireMaster, PartnerLogo, ProjectImage, ProjectMaster, SystemMaster, BeneficiaryCategory, ManagingListCategoryMaster, ListItemCategory, DropdownOption, EventMaster, BeneficiaryData
from import_export.admin import ImportExportModelAdmin
from django.utils import timezone
from django.utils.html import format_html


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




class Donationresources(resources.ModelResource):
    class Meta:
        model = Donation
        import_id_fields = ['id']
        fields = (
            'id',
            'receipt_number',
            'order_id',
            'name',
            'email',
            'mobile',
            'amount',
            'donation_type',
            'payment_method',
            'payment_status',
            'transaction_id',
            'paid_at',
            'pan_number',
            "address",
                "city",
                "state",
                "pincode",
                "country",
            'receipt_sent',
            'created_at',
        )


# -------------------------
# ADMIN PANEL
# -------------------------

class DonationAdmin(ImportExportModelAdmin):
    resource_class = Donationresources

    list_display = (
        'receipt_number',
        'order_id',
        'name',
        'email',
        'mobile',
        'formatted_amount',
        'donation_type',
        'colored_payment_status',
        'payment_method',
        'transaction_id',
        'paid_at_display',
        'receipt_sent',
        'created_at_display',
    )

    search_fields = (
        'receipt_number',
        'order_id',
        'name',
        'email',
        'mobile',
        'transaction_id',
        'pan_number',
    )

    list_filter = (
        'payment_status',
        'donation_type',
        'payment_method',
        'receipt_sent',
        'created_at',
    )

    ordering = ('-created_at',)

    list_per_page = 25

    readonly_fields = (
        'paid_at',
        'created_at',
    )

    # -------------------------
    # FIELD GROUPING
    # -------------------------

    fieldsets = (
        ("Donor Information", {
            "fields": (
                "name",
                "email",
                "mobile",
                "pan_number",
                "address",
                "city",
                "state",
                "pincode",
                "country",
            )
        }),

        ("Donation Details", {
            "fields": (
                "amount",
                "donation_type",
                "message",
            )
        }),

        ("Payment Details", {
            "fields": (
                "order_id",
                "payment_session_id",
                "payment_method",
                "payment_status",
                "transaction_id",
                "paid_at",
            )
        }),

        ("Receipt Details", {
            "fields": (
                "receipt_number",
                "receipt_sent",
                "created_at",
            )
        }),
    )

    # -------------------------
    # CUSTOM DISPLAY METHODS
    # -------------------------

    def formatted_amount(self, obj):
        return f"₹ {obj.amount:,.2f}"
    formatted_amount.short_description = "Amount"

    def colored_payment_status(self, obj):
        if obj.payment_status == "SUCCESS":
            color = "green"
        elif obj.payment_status == "FAILED":
            color = "red"
        else:
            color = "orange"

        return format_html(
            '<strong style="color:{};">{}</strong>',
            color,
            obj.get_payment_status_display()
        )
    colored_payment_status.short_description = "Payment Status"

    def paid_at_display(self, obj):
        if obj.paid_at:
            return timezone.localtime(obj.paid_at).strftime("%d %b %Y, %I:%M %p")
        return "-"
    paid_at_display.short_description = "Paid At"

    def created_at_display(self, obj):
        return timezone.localtime(obj.created_at).strftime("%d %b %Y, %I:%M %p")
    created_at_display.short_description = "Created At"


admin.site.register(Donation, DonationAdmin)
