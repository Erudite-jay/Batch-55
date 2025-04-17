from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . models import Contact
from .serializers import ContactSerializer

# Create your views here.

def print_hello(request):
    return HttpResponse("Hello World ! I am first Django View")

def homepage(request):
    return render(request,"Auth_app/index.html")

def all_data(request):
    if request.method=="GET":
        all_user_data=Contact.objects.all() #queryset
        sd=ContactSerializer(all_user_data,many=True) #sd 
        return JsonResponse({
            "success":True,
            "data":sd.data
        },status=200)