import time

from celery import shared_task
import logging


from interview.models import Interview
from services.ses import SESService


@shared_task
def delete_interview_from_db(interview_id):
    interviews = Interview.objects.get(id=interview_id)
    time.sleep(3)
    interviews.delete()


