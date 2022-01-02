from django.urls import path
from django.views.generic import TemplateView

app_name = "account"
urlpatterns = [
	# path("login", views.LoginView.as_view(), name="login"),
	path("index/", TemplateView.as_view(template_name = "account/Index.html"), name="Index")
]