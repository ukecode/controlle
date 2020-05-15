# format: utf-8
from django import forms
from django.contrib.auth.models import User
#from django.contrib.auth.forms import AuthenticationForm

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')
		widgets = {
			'username': forms.TextInput(attrs={'placeholder': 'Nome de Usuário'}),
			'password': forms.TextInput(attrs={'placeholder': 'Senha do Usuário'}),
		}