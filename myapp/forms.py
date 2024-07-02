from django import forms
from .models import *


class Form_Validation(forms.ModelForm):
    hobbies = forms.MultipleChoiceField(
        choices=Registration.data4,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Registration
        exclude = ['user']
      

class ChangePassword(forms.ModelForm):
    existing_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Existing Password"
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm Password"
    )
  


    class Meta:
        model = User
        fields = []  

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        existing_password = cleaned_data.get("existing_password")
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if not self.user.check_password(existing_password):
            self.add_error('existing_password', "The existing password is incorrect")

        if new_password != confirm_password:
            self.add_error('confirm_password', "The new passwords do not match")

        return cleaned_data


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["new_password"])
        if commit:
            user.save()
        return user
    

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))


class FirstLoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','pattern': '[^@\\s]+@[^@\\s]+\\.[^@\\s]+'}))
    

class ResetPasswordForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    temporary_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Temporary Password")
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="New Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirm New Password")

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password != confirm_password:
             self.add_error('confirm_password', "The new passwords do not match")
        return cleaned_data
    
class CreatePasswordForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="username")
    temporary_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Temporary Password")
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="New Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirm New Password")

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password != confirm_password:
            self.add_error('confirm_password', "The new passwords do not match")
        return cleaned_data
    
    
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'
    }))
    subject = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the subject'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5,
        'placeholder': 'Enter your message'
    }), required=True)
    
