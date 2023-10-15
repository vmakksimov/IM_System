from django.shortcuts import render
from rest_framework import generics
from interview.models import Interview
from interview.serializers import InterviewSerializer


# Create your views here.
class InterviewList(generics.ListAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


class InterviewUpdateView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


class CreateInterviewView(generics.ListCreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer