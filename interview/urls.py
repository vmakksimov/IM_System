from django.urls import path
from django.views.generic import TemplateView

app_name ='interview'

urlpatterns = (
    path('', TemplateView.as_view(template_name="interview/index.html")),
)