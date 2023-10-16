
from django.test import TestCase
from api_users.models import CustomModelUser
from .models import Interview
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

class Test_Create_Interview(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomModelUser.objects.create_user(
            email='vmakksimov@gmail.com', password='123456789', is_staff='True')
        Interview.objects.create(id=1, candidate_first_name='Viktor',
                                             candidate_last_name='Maksimov',
                                            date_for_interview='2023-10-25',
                                            email='vmakksimov@gmail.com',
                                            mobile_number='0899006831',
                                            gender='Male', status='Pending',
                                            is_staff='False')

    def test_interview_content(self):
        interview = Interview.objects.get(id=1)
        candidate_first_name = f'{interview.candidate_first_name}'
        candidate_last_name = f'{interview.candidate_last_name}'
        date_for_interview = f'{interview.date_for_interview}'
        email = f'{interview.email}'
        mobile_number = f'{interview.mobile_number}'
        gender = f'{interview.gender}'
        status = f'{interview.status}'
        is_staff = f'{interview.is_staff}'
        self.assertEqual(candidate_first_name, 'Viktor')
        self.assertEqual(candidate_last_name, 'Maksimov')
        self.assertEqual(email, 'vmakksimov@gmail.com')
        self.assertEqual(date_for_interview, '2023-10-25')
        self.assertEqual(mobile_number, '0899006831')
        self.assertEqual(gender, 'Male')
        self.assertEqual(is_staff, 'False')
        self.assertEqual(status, 'Pending')
        self.assertEqual(str(interview), "Viktor Maksimov")


class InterviewTests(APITestCase):

    def test_view_interview(self):
        """
        Ensure we can view all objects.
        """
        url = reverse('interview:create-interview')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_interview(self):
        """
        Ensure we can create a new Interview object and view object.
        """
        self.test_category = Interview.objects.create(candidate_first_name='Viktor', candidate_last_name='Maksimov',
                                            date_for_interview='2023-10-25',
                                            email='vmakksimov@gmail.com',
                                            mobile_number='0899006831',
                                            gender='Male', status='Pending',
                                            is_staff='False')
        self.testuser1 = CustomModelUser.objects.create_superuser(
            email='vmakksimov@gmail.com', password='123456789')


        self.client.login(email=self.testuser1.email,
                          password='123456789')

        data = {"candidate_first_name": "Viktor",
                "candidate_last_name": "Maksimov", "date_for_interview": "2023-10-25", "email": "vmakksimov@gmail.com",
                "mobile_number": "0899006831", "gender": "Male", "status": "Pending", "is_staff": "False"}
        url = reverse('interview:create-interview')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_interview_update(self):

        client = APIClient()

        self.test_category = Interview.objects.create(id=1, candidate_first_name='Viktor', candidate_last_name='Maksimov',
                                            date_for_interview='2023-10-25',
                                            email='vmakksimov@gmail.com',
                                            mobile_number='0899006831',
                                            gender='Male', status='Pending',
                                            is_staff='False')
        self.testuser1 = CustomModelUser.objects.create_superuser(
            email='vmakksimov@gmail.com', password='123456789')
        self.testuser2 = CustomModelUser.objects.create_user(
            email='ivan@abv.bg', password='123456789')

        client.login(email=self.testuser1.email,
                     password='123456789')

        url = reverse(('interview:modify-interviews'), kwargs={'pk': 1})

        response = client.put(
            url, {
                "id": 1, "candidate_first_name": "Viktor",
                "candidate_last_name": "Maksimov", "date_for_interview": "2023-10-25", "email": "vmakksimov@gmail.com",
                "mobile_number": "0899006831", "gender": "Male", "status": "Pending", "is_staff": "False"
            }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
