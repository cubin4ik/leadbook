from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class UserRegisterForm(UserCreationForm):
    fields = forms.EmailField

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
