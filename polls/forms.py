from django import forms

from .models import Task

class PostForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'done')