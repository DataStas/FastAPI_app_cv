import smtplib
from email.message import EmailMessage
from email.utils import formatdate

from celery import Celery

from config import SMTP_PASSWORD, SMTP_USER, REDIS_HOST, REDIS_PORT

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')


def get_email_template(username: str):
    email = EmailMessage()
    email['Subject'] = 'Отчёт'
    email['From'] = SMTP_USER
    email['Date'] = formatdate(localtime=True)
    email['To'] = SMTP_USER

    email.set_content(open('/pdfs/1.pdf').read())
    return email


@celery.task
def send_email_report(username: str):
    email = get_email_template(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)