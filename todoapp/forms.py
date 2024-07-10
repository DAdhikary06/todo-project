from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from todoapp.models import TODO
class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class TODOForm(forms.ModelForm):
    class Meta:
        model=TODO
        fields=['title','status','priority']
