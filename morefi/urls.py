
from django.contrib import admin
from django.urls import path
from office.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('office/',home),
    path('office/<esm>',sazman), 
]  
