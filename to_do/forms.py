from django import forms
from django.forms import ModelForm, widgets
from .models import *


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control mb-2 mr-sm-2', 'placeholder': 'Add Item'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
