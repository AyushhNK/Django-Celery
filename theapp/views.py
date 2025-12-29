from django.shortcuts import render
from .tasks import sub
from celery.result import AsyncResult

# Create your views here.
def index(request):
    print("results:")
    result=sub.delay(10, 4)
    print(result)
    return render(request, 'theapp/home.html', {'result': result})

def get_result(request, task_id):
    result = sub.AsyncResult(task_id)
    return render(request, 'theapp/result.html', {'result': result})