
from django.urls import path
from .views import RegisterViewAPI, BlacklistTokenView, UserViewSet

app_name ='api_users'

urlpatterns = [
    path('all/', UserViewSet.as_view({'get': 'list'}), name='all-users'),
    path('create/', RegisterViewAPI.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenView.as_view(),
         name='blacklist')
]