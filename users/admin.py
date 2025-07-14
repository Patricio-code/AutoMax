from django.contrib import admin
from .models import Profile, Locations
from localflavor.ar.forms import ARProvinceSelect, ARPostalCodeField
from django import forms
# Register your models here.

class LocationForm(forms.ModelForm):
    class Meta:

        zip_code = ARPostalCodeField()

        model = Locations
        fields = '__all__'
        widgets = {
            'state': ARProvinceSelect(),
        }

class ProfileAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    form = LocationForm
    list_display = ('address_1', 'address_2', 'state','city', 'zip_code')
    fields = ('address_1', 'address_2', 'state','city', 'zip_code')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Locations, LocationAdmin)