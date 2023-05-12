from django import forms
from .models import Task, University, Language, Hability

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