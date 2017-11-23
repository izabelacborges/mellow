from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def sign_up_request(request):
    return render(request, 'request.html')

def forgot_pass(request):
    return render(request, 'forgot.html')

def dashboard(request):
    return render(request, 'dashboard.html')