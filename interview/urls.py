

from django.urls import path

from .views import CreateInterviewView,InterviewUpdateView
from django.views.generic import TemplateView

app_name ='interview'


urlpatterns = (
    path('', TemplateView.as_view(template_name="index.html")),
    path('create/', CreateInterviewView.as_view(), name='create-interview'),
    path('update/<int:pk>', InterviewUpdateView.as_view(), name='modify-interviews'),
    # path('all/', InterviewList.as_view(), name='all-interviews'),
    # path('delete/<int:pk>', InterviewDeleteView.as_view(), name='delete-interview'),
)