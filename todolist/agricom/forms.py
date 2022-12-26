from django.forms import ModelForm
from .models import Agricom
from django import forms



class AgriComForm(ModelForm):
    
    MYCHOICE = (
        ("status", "STATUS"),
        ("pending", "PENDING"),
        ("done", "DONE")
    )
    
    PRINCIPAL = (
        ("principal", "PRINCIPAL"),
         ("yes", "YES"),
        ("no", "NO")
        
    )
    phone_number = forms.CharField(max_length=11, min_length=11,  widget=forms.TextInput(attrs={'placeholder' :'Number', 'style': 'width: 300px;', 'class': 'form-control'}), label="Email")
    names = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Location', 'style': 'width: 300px;', 'class': 'form-control'}))
    alternate_num = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Altenate Number', 'style': 'width: 300px;', 'class': 'form-control'}))
    
    status = forms.ChoiceField(choices=MYCHOICE)
    principal = forms.ChoiceField(choices=PRINCIPAL)
    class Meta:
        model = Agricom
        exclude = ['user',]
    