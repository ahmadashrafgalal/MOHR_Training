from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def SignUp(request):
    return render(request, 'Signup.html')