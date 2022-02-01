from django import forms
from .models import MyUser


class MyUserForm(form.ModelForm):
	class Meta:
		model = MyUser