from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def print_hello(request):
    return HttpResponse("Hello World ! I am first Django View")

def homepage(request):
    return render(request,"Auth_app/index.html")