from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['id']
        title = forms.CharField(widget=forms.TextInput
                                (attrs={'placeholder': 'Enter task'}))
