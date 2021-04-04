from django import forms
from readingTime.models import Profile, Contact
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegisterForm(UserCreationForm):
    # we inherite username, password1 and password2 from UserCreationForm
    # we then add the following extra fields:
    first_name = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password1', 'password2',)

class EditProfileForm(UserChangeForm):

    class Meta:
        # Register form based on the User form
        model = User
        fields = ('email', 'first_name', 'last_name',)

class ContactForm(forms.ModelForm):


    BookID=forms.CharField(max_length=30,required=True)
    BookTitle=forms.CharField(max_length=30,required=True)
    Author=forms.CharField(max_length=35,required=True)
    UploadImage=forms.FileField()

    class Meta:
        model = Contact
        fields = ('BookID', 'BookTitle', 'Author','UploadImage')
