from django.contrib import admin
from . models import Contact

# Register your models here.

# admin.site.register(Contact)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','message']
    search_fields=['email','name']
    list_filter=['email','name']