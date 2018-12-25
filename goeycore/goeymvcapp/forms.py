from django import forms
from django.core import validators
from django.contrib.auth.models import User
from goeymvcapp.models import Customer, UserProfileInfo

# Admin forms
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')



# FrontEnd forms
class SendEmailContactForm(forms.Form):
    first_name = forms.CharField(label='First name',max_length=20)
    last_name = forms.CharField(label='Last name', max_length=20)
    phone = forms.CharField(label='Phone', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    verify_email = forms.CharField(label='Verify Email', max_length=100)
    text_message = forms.CharField(
    max_length=500,
    widget=forms.Textarea(),
    help_text='Write here your message!'
    )

    def __str__(self):
        return self.first_name

# Customer Model Form
class CustomerRegisterForm(forms.ModelForm):
    class Meta():
        model = Customer
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'email', 'phone', 'password', 'vpassword']
