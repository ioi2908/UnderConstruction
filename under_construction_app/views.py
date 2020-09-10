from django.shortcuts import render, redirect
from .models import EmailNotify
from django.contrib import messages

def email_notify(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        object_email = EmailNotify()
        object_email.email = email
        if not '.com' in email:
            messages.error(request, 'Andika email yako kwa usahihi!')
            
        else:
            object_email.save()
            messages.success(request, 'Ahsante! Tunaifanyia kazi')
            
            
    return render(request, template_name='index.html')

def thanks(request):
    return render(request, template_name='thanks.html')