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
    email['To'] = email
    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, ваш отчет готов. Зацените 😊</h1>'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_email_report(username: str, email: str):
    email = get_email_template(username, email)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
        
@celery.task
def calculate_pdf(username: str, email: str, id: int):
    pass