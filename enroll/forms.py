from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Name','Department','Address','City','Email','Password']
        widgets = {
            'Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Department' : forms.TextInput(attrs={'class':'form-control'}),
            'Address' : forms.TextInput(attrs={'class':'form-control'}),
            'City' : forms.TextInput(attrs={'class':'form-control'}),
            'Email' : forms.EmailInput(attrs={'class':'form-control'}),
            'Password' : forms.PasswordInput(attrs={'class':'form-control'}),
        }
