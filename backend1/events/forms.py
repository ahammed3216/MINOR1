import email
from genericpath import exists
from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()

class LoginForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput())
    password=forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput())
    email=forms.CharField(widget=forms.EmailInput())
    password_one=forms.CharField(widget=forms.PasswordInput())
    password_two=forms.CharField(widget=forms.PasswordInput())


    def clean(self):
        cleaned_data=self.cleaned_data
        password_one=cleaned_data.get('password_one')
        password_two=cleaned_data.get('password_two')

        if password_one != password_two:
            raise forms.ValidationError("password doesnt match")
        return cleaned_data


    def clean_username(self):
        cleaned_data=self.cleaned_data
        username=cleaned_data.get('username')
        username_qs=User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        email_check=User.objects.filter(email=email)
        if email_check.exists():
            raise forms.ValidationError("Email alredy exists")
        return email
