import time

from celery import shared_task
import logging

from django.contrib.auth.models import User


@shared_task
def send_email_to_new_user(email):
    # SESService().send_email(email)
    # time.sleep(7)
    # logging.info('email was sent')
    print('asd')
    user = User.objects.get(email=email)
    user.last_name = 'SUCCESS2'
    time.sleep(10)
    user.save()