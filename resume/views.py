from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        context = {'name': name}

        # Send an Email
        send_mail(
            'from: ' + name + "About: " + subject,  # Subject
            message,  # Message
            email,  # From mail
            ['awuyadanielz@gmail.com'],  # To Mail
        )

        return render(request, 'resume/index.html', context)
    else:
        return render(request, 'resume/index.html')
