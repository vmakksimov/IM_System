from django.http import HttpResponse
from django.template import loader
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from .tasks import send_email_to_new_user

class RegisterViewAPI(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        template = loader.get_template('users/register.html')
        return HttpResponse(template.render({}, request))

    def post(self, request):
        data = {
            'email': request.data['email'],
            'password': request.data['password'],
            'password2': request.data['password2']
        }
        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                # TODO celery for later
                # send_email_to_new_user.delay(user.email)
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class BlacklistTokenView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
