from django import forms
from .models import User


class CUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'phone']
