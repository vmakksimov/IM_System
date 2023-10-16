import time

from celery import shared_task
import logging


from services.ses import SESService


@shared_task
def send_email_to_new_user(email):
    SESService().send_email(email)