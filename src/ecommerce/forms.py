from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control"}))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")

        return email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput())
    password_check = forms.CharField(
        widget=forms.PasswordInput())
    email = forms.EmailField()

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password_check = self.cleaned_data.get("password_check")
        if password != password_check:
            raise forms.ValidationError("Passwords dont match")

        return data

    def clean_username(self):
        username = self.cleaned_data.get("username")

        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")

        return username
