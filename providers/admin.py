from django.contrib import admin
from . import models
# Register your models here.


class ContactInline(admin.StackedInline):
    model = models.ProviderContact
    extra=0
    readonly_fields = ['name','last_name','rol','email','phone','mob']



class SocialInline(admin.TabularInline):
    model = models.SocialLink
    extra=0
    readonly_fields = ['name','link']



class ServiceInline(admin.TabularInline):
    model = models.ServiceInformation
    extra=0
    
    
    
    readonly_fields = ['service_type','service_description','review_aggreement','status']

# admin.site.register(models.Provider)

@admin.register(models.Provider)
class ProviderAdmin(admin.ModelAdmin):

    def provider_contact_name(self, obj):
        return f'{obj.providercontact.name} {obj.providercontact.last_name}'

    def provider_contact_phone(self, obj):
        return obj.providercontact.phone

    def service_status(self, obj):
        return obj.serviceinformation.get_status_display()
    def service_name(self, obj):
        return obj.serviceinformation.get_service_type_display()

    list_display = ['public_name','service_name','provider_contact_name','provider_contact_phone','service_status']
    inlines = (SocialInline,ContactInline,ServiceInline )
    change_form_template = 'admin/change_form.html'
    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.readonly_fields = [field.name for field in obj.__class__._meta.fields]
        return self.readonly_fields


