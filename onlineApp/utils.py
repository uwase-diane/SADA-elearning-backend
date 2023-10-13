from email.message import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth import get_user_model
import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def get_tokens_for_user(user):

    print("user")
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access_token' : str(refresh.access_token),
    }


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        EmailThread(email).start()