from django.test import TestCase

from django.test import TestCase
from api_users.models import CustomModelUser
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

class Test_Create_User(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomModelUser.objects.create_user(
            email='vmakksimov@gmail.com', is_staff='True')

    def test_user_content(self):
        user = CustomModelUser.objects.get(id=1)
        email = f'{user.email}'
        is_staff = f'{user.is_staff}'
        self.assertEqual(email, 'vmakksimov@gmail.com')
        self.assertEqual(is_staff, 'True')

