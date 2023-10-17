import logging
import boto3
class SESService():

    def __init__(self):
        self.client = boto3.client(
            'ses',
            aws_access_key_id="INPUT YOUR ACESS KEY FROM AWS",
            aws_secret_access_key="INPUT YOUR SECRET ACESS KEY FROM AWS",
            region_name="INPUT YOUR REGION",
        )

    @staticmethod
    def __verify_status(*email):
        approved_message = 'We are happy to inform you that your application was approved'
        rejected_message = 'We regret to inform you that your application was rejected'
        application = 'Thank you for applying. We will get back to you as soon as possible!'
        status = application
        if len(email) > 1 and email[1] == 'Approved':
            status = approved_message
        elif len(email) > 1 and email[1] == 'Rejected':
            status = rejected_message
        return status

    def send_email(self, *email):
        message = self.__verify_status(*email)
        response = self.client.send_email(
            Source='bignightmare1@gmail.com',
            Destination={
                'ToAddresses': [
                    email[0],
                ],

            },
            Message={
                'Subject': {
                    'Data': f'Welcome to Interview Management System {email[0]}!',
                    'Charset': 'UTF-8'
                },

                'Body': {
                    'Text': {

                        'Data': f'{message}',
                        'Charset': 'UTF-8'
                    }

                }
            },
        )
        logging.info(f'Email sent {response}')


