from django.urls import path
from .views import handle_file_upload

urlpatterns=[
path('file/',handle_file_upload)
]