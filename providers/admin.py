from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.ServiceInformation)
admin.site.register(models.ProviderContact)
admin.site.register(models.SocialLink)


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
    
    inlines = (ContactInline,ServiceInline,SocialInline )
    change_form_template = 'admin/change_form.html'
    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.readonly_fields = [field.name for field in obj.__class__._meta.fields]
        return self.readonly_fields

    # readonly_fields = get_readonly_fields()

