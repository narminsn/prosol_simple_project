from django import forms
from . import models


class ProviderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = models.Provider
        fields = "__all__"
        # exclude = ("status",)



class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = models.ProviderContact
        fields = '__all__'


class ServiceInfo(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = models.ServiceInformation
        fields = '__all__'
        