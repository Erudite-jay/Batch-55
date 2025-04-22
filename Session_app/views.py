from django.http import JsonResponse
from django.shortcuts import render
from . models import UserData
# Create your views here.


def login_view(request):
    if request.session.get('username'):
        return JsonResponse({
            "Success":True,
            "Message":"User already logged in",
            "user is": request.session.get('username')
        },status=200)
    
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        try:
            user=UserData.objects.get(username=username)

            if user.password==password: 
                request.session['username']=username
                request.session.set_expiry(20)
                return JsonResponse({
                    "success":True,
                    "Message":"User logged in successfully"
                },status=200)
            
        except Exception as e:
            return JsonResponse({
                "suucess":False,
                "Error":str(e)
            },status=500)
        
    return render(request,"Session_app/login.html")