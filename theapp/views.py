from django.shortcuts import render

# Create your views here.
def index(request):
    print("results:")
    return render(request, 'theapp/home.html')