from django.http import JsonResponse
from django.shortcuts import render
from .forms import FileForm
from .models import File

# Create your views here.

def handle_file_upload(request):
    if request.method=="POST":
        form =FileForm(request.POST,request.FILES) #file #nameOfTheFile
        print(form)
        if form.is_valid(): #if form data is valid
            #normal form
            # record=File(name=form.cleaned_data['name'],file=form.cleaned_data['file'])
            # record.save()

            #model form
            form.save()
            return JsonResponse({
                "success":True,
            },status=201)
        
    else:
        form =FileForm() #empty form

    return render(request,"Forms_app/file_upload_form.html",{'form':form})