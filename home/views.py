from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from home.models import Appointment

# Create your views here.
def index(request):
    return render(request,'index.html')

def appointment(request):
    if request.method == "POST":
        firstname= request.POST.get('firstname')
        lastname= request.POST.get('lastname')
        gender= request.POST.get('gender')
        phone= request.POST.get('phone')
        email= request.POST.get('email')
        date = request.POST.get('date')
        checkbox = request.POST.get('checkbox')
        mail = request.POST.get('mail')
        appointment= Appointment(firstname=firstname, lastname=lastname, gender=gender, phone=phone, email=email, date=date, checkbox=checkbox, mail=mail)
        appointment.save()
    return render(request,'appointment.html')

def aboutus(request):
    return render(request,'aboutus.html')

def explore1(request):
    return render(request,'explore1.html')

def contactus(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        comment= request.POST.get('comment')
        contactus= Contact(name=name, email=email, comment=comment)
        contactus.save()
    return render(request,'contactus.html')

