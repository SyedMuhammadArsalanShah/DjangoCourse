from django.shortcuts import render, HttpResponse

from home.models import Contact
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name =request.POST.get("username")
        email =request.POST.get("email")
        contact =request.POST.get("contact")
        message =request.POST.get("message")
        obj = Contact(name=name, email=email, contact=contact, message=message, date=datetime.today())
        obj.save()
        return HttpResponse("created")
    return render(request, "contact.html")

def service(request):
    return HttpResponse("this is my service page")
    # return render(request, "service.html")