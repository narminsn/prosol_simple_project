from django.urls import path
from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home' ),
    path('providers/', views.provider_apply, name='providers'),
    path('providers/confirm/<int:id>/<str:status>', views.confirm_provider, name='confirm_provider'),


]
