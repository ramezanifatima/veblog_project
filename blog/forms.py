from django import forms
from  . import models


class MassageForm(forms.ModelForm):
    class Meta:
        model = models.Massage
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام'
            }),
            "email": forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            }),
            "phonnumber": forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'شماره تلفن'
            }),
            "titl": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'موضوع'
            }),
            "body": forms.Textarea(attrs={
                'placeholder': 'متن'
            })

        }
