
from django.urls import include, path
from . import views

urlpatterns = [
    path('p-h/',views.print_hello),
    path('home/',views.homepage)
]