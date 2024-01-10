from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

CLASSES = 'shadow appearance-none border rounded-2xl w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class':'shadow appearance-none border rounded-2xl w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
    }))
        
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':'shadow appearance-none border rounded-2xl w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
    }))



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Username',
        'class':CLASSES
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your Email',
        'class':CLASSES
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':CLASSES
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Retype Password',
        'class':CLASSES
    }))
