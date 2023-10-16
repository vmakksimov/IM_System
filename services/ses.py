import logging

import boto3

class SESService():
    def __init__(self):
        self.client = boto3.client(
            'ses',
            aws_access_key_id="AKIA3SBSR3XE4SVZCUBU",
            aws_secret_access_key="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",
            region_name="eu-central-1",
        )


    def send_email(self, email):
        response = self.client.send_email(
            Source='bignightmare1@gmail.com',
            Destination={
                'ToAddresses': [
                    email,
                ],

            },
            Message={
                'Subject': {
                    'Data': f'Welcome to Interview Management System {email}!',
                    'Charset': 'UTF-8'
                },
                
                'Body': {
                    'Text': {

                        'Data': f'Thank you for registering. Enjoy your journey, {email}!',
                        'Charset': 'UTF-8'
                    }

                }
            },
        )
        logging.info(f'Email sent {response}')