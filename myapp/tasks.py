from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    """Background task to send an email"""
    send_mail(
        "Welcome to Our Platform",
        "Thank you for signing up!",
        "from@example.com",
        [user_email],
        fail_silently=False,
    )
    return f"Email sent to {user_email}"
