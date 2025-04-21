from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . models import Contact
from .serializers import ContactSerializer
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.

def print_hello(request):
    return HttpResponse("Hello World ! I am first Django View")

def homepage(request):
    return render(request,"Auth_app/index.html")

@csrf_exempt
def all_data(request):
    if request.method=="GET":
        all_user_data=Contact.objects.all() #queryset
        sd=ContactSerializer(all_user_data,many=True) #sd 
        return JsonResponse({
            "success":True,
            "data":sd.data
        },status=200)
    
    if request.method=='POST':
        input_data=json.loads(request.body) #json
        # json -> qs
        sd=ContactSerializer(data=input_data) 
        if sd.is_valid():
            sd.save()
            return JsonResponse({
                "success":True,
                "message":"Data Saved successfully"
            },status=201)

@csrf_exempt
def single_user_data(request,pk):

    if request.method=="GET":
        try:
            user=Contact.objects.get(pk=pk) #single object in a QS
            sd=ContactSerializer(user) #serilaization
            return JsonResponse({
               " success":True,
               "data":sd.data
            },status=200)
        
        except Exception as e:
            return JsonResponse({
                "Success":False,
                "Error":str(e)
            },status=500)
        
    if request.method=="PUT":
        try:
            input_data=json.loads(request.body)
            user=Contact.objects.get(pk=pk)

            sd=ContactSerializer(user,data=input_data)

            if sd.is_valid():
                sd.save()
                return JsonResponse({
                    "Success":True,
                    "Message":"user updated successfully"
                },status=200)
            
            return JsonResponse(sd.errors, status=400)
            
        except Exception as e:
            return JsonResponse({
                "Success":False,
                "Error": str(e.as_json())
            },status=500)
        
    if request.method=="PATCH":
        try:
            input_data=json.loads(request.body)
            user=Contact.objects.get(pk=pk)

            sd=ContactSerializer(user,data=input_data,partial=True)

            if sd.is_valid():
                sd.save()
                return JsonResponse({
                   "success":True,
                   "Message":"Partial update is Done"
                },status=200)
            return JsonResponse(sd.errors, status=400)
        except user.DoesNotExist:
            return JsonResponse({
                "Success":False,
                "Message":"User Doesn't exist",
                "PK":pk
            }, status=404)
        except Exception as e:
            return JsonResponse({
                "Success":False,
                "Error": str(e.as_json())
            },status=500)
        finally:
            return JsonResponse({
               "Message":"Hii You have reached here"
            })
        
    if request.method=="DELETE":
        user=Contact.objects.get(pk=pk)
        user.delete()
        return JsonResponse({
           "success":True
        })