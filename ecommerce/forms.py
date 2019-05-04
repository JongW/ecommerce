from django import forms


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