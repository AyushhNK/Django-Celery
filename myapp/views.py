from django.http import JsonResponse
from myapp.tasks import send_welcome_email

def send_email_view(request):
    """Triggers the Celery email task"""
    user_email = request.GET.get("email", "test@example.com")
    send_welcome_email.delay(user_email)  # Run task asynchronously
    return JsonResponse({"message": "Email is being sent!"})
