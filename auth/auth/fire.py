import os
from django.http.response import HttpResponse
from django.urls import path
from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'abcsdd-e95cf-firebase-adminsdk-j865h-5e1e5867df.json')
cred = credentials.Certificate(file_path)
firebase_admin.initialize_app(cred)



def isValidToken(request):
    id_token = request.headers["Authorization"]
    print("=================================================start id token============================")
    print(id_token)
    
    try:
        print("=================================================start decoded token============================")
        decoded_token = auth.verify_id_token(id_token) 
        print(decoded_token)
        return decoded_token
    except:
        return  
