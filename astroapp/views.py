from django.shortcuts import render,redirect
from .models import *
import sweetify


def home(request):
    if request.method =='POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact_form.objects.create(name=name , email=email , message=message, subject=subject, lastname=lastname)
        sweetify.success(request, 'Thank you!', text='Your message has been sent.', persistent='Close')
        
        return redirect(home)
    
    
    return render(request,'index.html')


    


