from django import forms
from .models import Task, University, Language, Hability
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'category', 'done']

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name', 'rank', 'email', 'description']

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['title', 'proficiency', 'description']

class HabilityForm(forms.ModelForm):
    class Meta:
        model = Hability
        fields = ['title', 'level']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 