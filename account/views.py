from django.contrib import auth
from django.shortcuts import render

class MyLoginView(auth.LoginView):
	template_name = "account/login.html"
	
