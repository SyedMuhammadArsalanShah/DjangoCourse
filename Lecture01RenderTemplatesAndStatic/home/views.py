from django.shortcuts import render, HttpResponse

# Create your views here.




def index(request):
    context ={
        "name":"Ammarah Asif",
        "age":"20",
        "contact": 124
    }
    return render(request, "index.html",context)
    # return HttpResponse("My first web")


def about(request):
    return render(request, "about.html")
    # return HttpResponse("My first aboutweb")


def contact(request):
    return render(request, "contact.html")
    # return HttpResponse("My first contact web")

