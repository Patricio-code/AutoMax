from django.db import models
from django.contrib.auth.models import User
from localflavor.ar.forms import PROVINCE_CHOICES
from .utils import user_directory_path
# Create your models here.

class Locations(models.Model):
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length= 64)
    state = models.CharField(max_length=64, choices=PROVINCE_CHOICES, default='')
    zip_code = models.CharField(max_length= 10, default='')

    def __str__(self):
        return f'Location {self.id}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path ,null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    location = models.OneToOneField(Locations, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f'{self.user.username}\'s Profile' #esto es para que en el panel del admin, dentro del modelo Profile, aparezca el nombre del usuario y no Profile object
     