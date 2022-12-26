from django.forms import ModelForm
from .models import BlogTask
from django import forms


class DataForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description', 'style': 'width: 300px;', 'class': 'form-control'}))
    class Meta:
        model = BlogTask
        exclude = ['user',]
        


    
    