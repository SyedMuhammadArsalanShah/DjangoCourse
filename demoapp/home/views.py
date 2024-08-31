
from django.shortcuts import render ,HttpResponse

# Create your views here.


def index(request):
    
    context ={
        "name":"Ammarah Asif",
        "age":"20",
        "contact": 124
    }
    return render(request, "index.html",context)
    # return HttpResponse("this is my first page")


def about(request):
    return HttpResponse("this is my about page")


def service(request):
    return HttpResponse("this is my service page")




