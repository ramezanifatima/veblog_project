from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError
from django.contrib.auth.models import User

class LoginForm (forms.Form):
    username = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'رمز '}))

    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username'),password= self.cleaned_data.get('password'))
        if user is not None :
            return self.cleaned_data.get('password')
        raise ValidationError('username or password ar wrong ', code='invalid info')

class SigninForm(forms.Form):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'نام'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}))
    email = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز'}))
    passwordagain = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار رمز'}))




class UserEditeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

