from django import forms
from .models import Task


class AddTask(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['content']
        labels = {'content':''}

        
        
    
