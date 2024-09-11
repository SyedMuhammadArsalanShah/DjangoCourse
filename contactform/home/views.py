from datetime import datetime
from django.shortcuts import render ,HttpResponse

from home.models import Contact

# Create your views here.



def index(request):
    # return HttpResponse("this is my home page")
    context={"name":"Ammmarah Asif",
              "Age":20,
              "email":"aa@gmail.com", 
              "address":"karachi",
              "contact":15
              
              
              }
    return render(request, "index.html", context)



def contact(request):
    if request.method == "POST":
        email= request.POST.get("email")
        desc= request.POST.get("desc")

        obj= Contact(email=email, desc=desc, dateofpost=datetime.today())
        obj.save()
        return HttpResponse("created user")
    return render(request, "contact.html")



def about(request):
    # return HttpResponse("this is my about page")
    return render(request, "about.html")



def service(request):
    return HttpResponse("this is my service page")