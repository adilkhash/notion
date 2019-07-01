from django.urls import path
from django.views.generic import TemplateView

from apps.courses.views import create_luigi_invoice

app_name = 'courses'
urlpatterns = [
    path('luigi/', TemplateView.as_view(template_name='courses/index.html'),
         name='luigi-course'),
    path('luigi/create-invoice', create_luigi_invoice, name='luigi-create-invoice'),
]
