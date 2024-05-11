import time

from celery import shared_task
import logging
from interview.models import Interview
from services.ses import SESService
@shared_task
def send_email_to_user(*email):
    SESService().send_email(*email)

@shared_task
def delete_interview_from_db(interview_id):
    interview = Interview.objects.get(id=interview_id)
    interview.delete()


