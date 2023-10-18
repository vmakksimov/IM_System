
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from schema_graph.views import Schema
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('interview.urls', namespace='interview')),
    path('api/user/', include('api_users.urls', namespace='api_users')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', include_docs_urls(title='InterviewAPI')),
    path('schema', get_schema_view(title='InterviewAPI', description='API for Interview', version="1.0.0"), name='openapi-schema'),
    path('schema-graph/', Schema.as_view()),
]
