
from django.urls import path
from .views import RegisterViewAPI, BlacklistTokenView

app_name ='api_users'

urlpatterns = [
    path('create/', RegisterViewAPI.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenView.as_view(),
         name='blacklist')
]