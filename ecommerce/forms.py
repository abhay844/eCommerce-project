from django import forms
from django.contrib.auth import get_user_model

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Your full name"
                }
                )
            )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control","placeholder":"Your email address"
                }
                )
            )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control","placeholder":"Your content"
                }
                )
            )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if "gmail.com" not in email:
            raise forms.ValidationError("Email has to be gmail.com")
        
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

User = get_user_model()
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)

        if qs.exists():
            raise forms.ValidationError("User already exits")

        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)

        if qs.exists():
            raise forms.ValidationError("email already exits")
            
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Passwords are not matching")
        
        return data