from django import forms
from .models import UserRegistration

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
