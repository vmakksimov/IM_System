from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer

from interview.models import Interview
from interview.serializers import InterviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class InterviewList(generics.ListAPIView):
    queryset = Interview.objects.all()
    # renderer_classes = [TemplateHTMLRenderer]
    serializer_class = InterviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        interviews = Interview.objects.all().values()
        context = {
                'interview': interviews
            }
        template = loader.get_template('interview/all.html')
        return HttpResponse(template.render(context, request))



class InterviewUpdateView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


class CreateInterviewView(generics.ListCreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

