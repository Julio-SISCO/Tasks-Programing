from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus' : 'True', 'class' : 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus' : 'True', 'class' : 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))



class TaskForm(forms.Form):
    class Meta:
        model = models.Task
        fields = ['owner', 'label', 'description', 'begin', 'end', 'priority', 'done']
        widgets = {
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
            'label': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'begin': forms.DateInput(attrs={'class': 'form-control'}),
            'end': forms.DateInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'done': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
