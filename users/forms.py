from django import forms
from .models import Locations, Profile
from django.db import models
from django.contrib.auth.models import User
from .widgets import CustomPictureImageFieldWidget

class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget, required=False)
    bio = forms.TextInput()

    class Meta:
        model = Profile
        fields = ('photo', 'bio','phone_number')

class LocationForm(forms.ModelForm):

    address_1 = forms.CharField(required=True)
    zip_code = models.CharField(max_length= 10, default='')

    class Meta:
        model = Locations
        fields = {'address_1','address_2','city','state','zip_code'}

