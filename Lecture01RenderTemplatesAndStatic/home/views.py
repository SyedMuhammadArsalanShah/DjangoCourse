from django.shortcuts import render, HttpResponse

# Create your views here.




def index(request):
    return render(request, "index.html")
    # return HttpResponse("My first web")


def about(request):
    return HttpResponse("My first aboutweb")


def contact(request):
    return HttpResponse("My first contact web")

