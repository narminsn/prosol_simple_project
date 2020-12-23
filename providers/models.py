from django.db import models

# Create your models here.

class Provider(models.Model):
    public_name = models.CharField(max_length=100)
    legal_name = models.CharField(max_length=100, null=True,blank=True)
    company_website = models.CharField(max_length=100, null=True,blank=True)
    company_phone = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    company_description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.public_name

    class Meta:
        verbose_name = 'Provider Information'
        verbose_name_plural = 'Provider Informations'

    

class SocialLink(models.Model):
    social_type = (
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),

    )
    provider = models.ForeignKey(Provider,on_delete=models.CASCADE)
    name = models.CharField(max_length=40,choices=social_type)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
    

    
class ProviderContact(models.Model):
    provider = models.OneToOneField('Provider',on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rol = models.CharField(max_length=100, null=True,blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100,null=True,blank=True)
    mob = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.last_name}'
    
    class Meta:
        verbose_name = 'Main Contact'
        verbose_name_plural = 'Main Contacts'


class ServiceInformation(models.Model):


    type_choices = [
        ('transfer', 'Transfer'),
        ('rent', 'Rent a car'),
    ]

    status_choices = (
        ('0', 'Waiting'),
        ('1', 'Approve'),
        ('2', 'Cancel'),
    
    )
    provider = models.OneToOneField('Provider',on_delete=models.CASCADE,null=True,blank=True)
    service_type = models.CharField(max_length=40, choices=type_choices)
    service_description = models.TextField()
    review_aggreement = models.BooleanField()
    status = models.CharField(max_length=40, choices=status_choices,default='0',blank=True)


    class Meta:
        verbose_name = 'Service Information'
        verbose_name_plural = 'Service Informations'

    def __str__(self):
        return self.service_type