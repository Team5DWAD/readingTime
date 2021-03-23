from django import forms
from readingTime.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
'''
class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(), required=True)
    first_name = forms.CharField(widget=forms.TextInput(), required=True)
    last_name = forms.CharField(widget=forms.TextInput(), required=True)
    username = forms.CharField(widget=forms.TextInput(), required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    password_repeat = forms.CharField(widget=forms.PasswordInput(), required=True)   
'''

class RegisterForm(UserCreationForm):
    # we inherite username, password1 and password2 from UserCreationForm
    # we then add the following extra fields:
    first_name = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password1', 'password2',)

