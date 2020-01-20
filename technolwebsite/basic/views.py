from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'homePage.html')

def about(request):
    return render(request,'about us.html')


def history(request):
    return render(request,'history.html')

def services(request):
    return render(request,'services.html')

def training(request):
    return render(request,'training.html')