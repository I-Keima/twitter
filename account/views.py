from django.contrib.auth.views import LoginView
from django.shortcuts import render

class MyLoginView(LoginView):
	template_name = "account/login.html"

