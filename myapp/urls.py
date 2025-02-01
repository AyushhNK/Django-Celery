from django.urls import path
from myapp.views import send_email_view

urlpatterns = [
    path("send-email/", send_email_view, name="send_email"),
]
