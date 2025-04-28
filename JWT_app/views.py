from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

def login_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)  #admin admin

        if user is not None:
            token = RefreshToken.for_user(user)
            return JsonResponse({
                "success":True,
                'refresh': str(token),
                'access': str(token.access_token),
            },status=200)
        

    return render(request,'JWT_app/login.html')