
from rest_framework import generics, status
from api_users.tasks import delete_interview_from_db, send_email_to_user
from services.ses import SESService
from api_users.models import CustomModelUser
from interview.models import Interview
from interview.serializers import InterviewSerializer
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser, \
    DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS, DjangoModelPermissions
from rest_framework.response import Response

# Create your views here.
class InterviewUpdateView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [DjangoModelPermissions]

    def post(self, request, pk):
        interview = Interview.objects.get(id=pk)
        new_status = request.data['status']
        interview.status = request.data['status']
        interview.email = request.data['email']
        interview.date_for_interview = request.data['date_for_interview']
        interview.candidate_first_name = request.data['candidate_first_name']
        interview.candidate_last_name = request.data['candidate_last_name']
        interview.mobile_number = request.data['mobile_number']
        interview.gender = request.data['gender']
        serializer = InterviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        interview.save()
        if new_status == 'Approved' or new_status == 'Rejected':
            ### TODO unmark to send email notification according to the status of the application
            #send_email_to_user.delay(interview.email, new_status)
            delete_interview_from_db.delay(interview.id)
        return Response(status=status.HTTP_200_OK)

class CreateInterviewView(generics.CreateAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [IsAdminUser]

class InterviewAPIList(generics.ListAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [IsAdminUser]



