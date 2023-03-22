from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def lewis(request):
    return HttpResponse("Hello, Lewis!")
def gimp(request):
    return HttpResponse("Hello, gimp!")
#def greet(request, name):
 #   return HttpResponse(f"Hello, {name.capitalize()}!")
def greet1(request, name):
    return render(request,"hello/greet.html",{
        "name": name.capitalize()
    })