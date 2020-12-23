from django.shortcuts import render,redirect
from .forms import ProviderForm, ContactForm, ServiceInfo
# Create your views here.
from django.http import JsonResponse
from django.views import generic
from . import models
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages



def providers(request):
    context = {
        'form' : ProviderForm,
        'contact_form' : ContactForm,
        'service_form' : ServiceInfo
    }
    return render(request, 'providers.html',context)

def provider_apply(request):
    context = {}
    context['form'] = ProviderForm
    context['contact_form'] = ContactForm
    context['service_form'] = ServiceInfo
    # context_object_name = 'new_apps_list'
    if request.method == "POST":
        form = ProviderForm(request.POST)
        social = request.POST.getlist('social_link')
        link = request.POST.getlist('link_value')
        print(social)
        print(link,'\n\nsdfASJd')
        if form.is_valid() and social[0] and link[0]:
            provider = form.save()
            social_value = []
            for index,field in enumerate(social):
                models.SocialLink.objects.create(provider_id=provider.id,name=social[index],link=link[index])
                obj = {
                    'value' : social[index],
                    'link' : link[index]
                }
                social_value.append(obj)



            contact_form = ContactForm(request.POST)
            
            if contact_form.is_valid():
                contact = contact_form.save(commit=False)
                contact.provider_id = provider.id
                contact.save()

                service_form = ServiceInfo(request.POST)
                if service_form.is_valid():

                    service = service_form.save(commit=False)
                    service.provider_id = provider.id
                    service.save()
                    if service.review_aggreement:
                        return redirect('/')
                    else:
                        contact.delete()
                        provider.delete()
                        service.delete()

                        context['checkbox_error'] = True
                        context['social_value'] = social_value

                        context['form'] = ProviderForm(request.POST)
                        context['contact_form'] = ContactForm(request.POST)
                        context['service_form'] = ServiceInfo(request.POST)

                else:

                    contact.delete()
                    provider.delete()

                    context['social_value'] = social_value
                    context['form'] = ProviderForm(request.POST)
                    context['contact_form'] = ContactForm(request.POST)
                    context['service_form'] = ServiceInfo(request.POST)


            else:
                provider.delete()
                context['form'] = ProviderForm(request.POST)
                context['social_value'] = social_value
                context['contact_form'] = ContactForm(request.POST)
                context['service_form'] = ServiceInfo(request.POST)


        else:
            context['social_value_error'] = True
            context['form'] = ProviderForm(request.POST)
            context['contact_form'] = ContactForm(request.POST)
            context['service_form'] = ServiceInfo(request.POST)
            
    
    return render (request, 'providers.html',context)
            


# Provider Status Confirm by admin

@staff_member_required
def confirm_provider(request,id,status):
    try:
        data = models.Provider.objects.filter(id=id).first().serviceinformation
        print(data.status,data.id,'DATA\n\n')
        data.status = status
        data.save()
        print(data.status,data.id,'DATA\n\n')

        return redirect(f'/admin/providers/provider/{id}/change')
    except:
        messages.error(
            request, "The operation could not be performed"
        )
        return redirect('/admin/providers/provider')

