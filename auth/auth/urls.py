"""auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from auth.settings import BASE_DIR
from django.contrib import admin
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import path
from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from auth.fire import isValidToken

def login(request):
    return render(request,"login.html")

def create(request):
    return render(request,"create.html")

def verify(request):
    return render(request,"verify.html")

def home(request):
   if(isLoggedIn(request)==False):
       return HttpResponseRedirect("/login")

   return HttpResponse("hi there,you are now logged in")


def create_session(request):
    user=isValidToken(request)
    if(user):
        request.session["user"]=user
        return JsonResponse({"success":True})
    else:
        return JsonResponse({"success":False})


def isLoggedIn(request):
    try:
        request.session['user']
        return True
    except:
        return False
  

urlpatterns = [
    path('verify/', verify),
    path('create/', create),
    path('login/', login),
    path('home/',home),
    path('create_session/',create_session)
]


