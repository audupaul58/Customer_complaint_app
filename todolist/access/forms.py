from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms



class LoginUser(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginUser, self).__init__(*args, **kwargs)
        
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}))
       



class CreateUser(UserCreationForm):
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;', 'class': 'form-control'}), label="Email")
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;', 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'style': 'width: 300px;', 'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('email','username', 'password1', 'password2')
