from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={'type':'tezt', 'class':'form-control'}))
    last_name = forms.CharField(max_length=101, widget=forms.TextInput(attrs={'type':'text', 'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'type':'email', 'class':'form-control'}))
    password1 = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(attrs={'type':'password','class':'form-control'}))
    password2 = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput(attrs={'type':'password','class':'form-control'}))
    user_type = forms.ChoiceField(choices=User.UserType.choices, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',
                  'password1', 'password2', 'user_type']


class LoginForm(forms.Form):
    email = forms.CharField(max_length=120, required=True, widget=forms.TextInput(attrs={'type':'email','class':'form-control'}))
    password = forms.CharField(max_length=120, min_length=1,
                               widget=forms.TextInput(attrs={'type':'password', 'class':'form-control'}))
