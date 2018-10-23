from django import forms
from .models import signup_model

class signup_form(forms.ModelForm):
    class Meta:
        model=signup_model
        fields=['username','email','password','details']

class LoginForm(forms.ModelForm):

      class Meta:
        model = signup_model
        fields = ['username', 'password']