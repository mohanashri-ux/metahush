from django import forms
from .models import UserRegistration
from .models import PetSittingService

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class PetSittingServiceForm(forms.ModelForm):
    class Meta:
        model = PetSittingService
        exclude = ['cost']  # do NOT include 'cost' in the form
        widgets = {
            'from_date': forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'}),
        }
