from django.shortcuts import render
from .tasks import sub

# Create your views here.
def index(request):
    print("results:")
    result=sub.delay(10, 4)
    print(result)
    return render(request, 'theapp/home.html', {'result': result.get()})