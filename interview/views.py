from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from rest_framework import generics, status
from rest_framework.renderers import TemplateHTMLRenderer

from api_users.models import CustomModelUser
from interview.models import Interview
from interview.serializers import InterviewSerializer
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser, \
    DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class InterviewWritePersmission(BasePermission):
    message = 'Only interviews and admins are allowed to delete'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.email == request.user

# class InterviewList(generics.ListAPIView):
#     queryset = Interview.objects.all()
#     # renderer_classes = [TemplateHTMLRenderer]
#     serializer_class = InterviewSerializer
#     permission_classes = [IsAdminUser]
#
#     def get(self, request, *args, **kwargs):
#         interviews = Interview.objects.all().values()
#         context = {
#                 'interview': interviews
#             }
#         template = loader.get_template('interview/all.html')
#         return HttpResponse(template.render(context, request))

class InterviewUpdateView (generics.RetrieveUpdateDestroyAPIView, InterviewWritePersmission):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [DjangoModelPermissions]

# class InterviewDeleteView (generics.DestroyAPIView, InterviewWritePersmission):
#     queryset = Interview.objects.all()
#     serializer_class = InterviewSerializer
#     permission_classes = [DjangoModelPermissions]
#
#     def get(self, request, pk):
#         interview = Interview.objects.get(id=pk)
#         serializer = InterviewSerializer(interview)
#         return Response(serializer.data)

class CreateInterviewView(generics.ListCreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [AllowAny]



