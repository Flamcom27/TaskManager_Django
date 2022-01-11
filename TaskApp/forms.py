from django import forms
from .models import *


class TaskForm(forms.Form):
    title = forms.CharField(max_length=30, label='Task')
    description = forms.CharField(max_length=250, required=False)
    deadline = forms.DateField(required=False)
    done = forms.BooleanField(required=False)
