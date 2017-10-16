from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def sign_up_request(request):
    return render(request, 'sign_up_request.html')