
from django.urls import include, path
from . import views

urlpatterns = [
    path('p-h/',views.print_hello),
    path('home/',views.homepage),
    path('data/',views.all_data),
    path('sud/<int:pk>/',views.single_user_data)
]