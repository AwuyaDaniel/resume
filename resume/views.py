from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, 'resume/index.html')
