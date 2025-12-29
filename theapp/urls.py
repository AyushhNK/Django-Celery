from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('result/<str:task_id>/', views.get_result, name='get_result'),
]