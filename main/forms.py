#acá armo formularios customizados

from django import forms
from .models import ListingModel

class ListingForm(forms.ModelForm):
    image = forms.ImageField(required=False)# Django por defecto reconoce el tipo de dato que necesito ingresar viendo el modelo, pero yo puedo customizarlo. Por ejemplo, en este caso, settié que la imagen no sea requerida
    
    class Meta:
        model = ListingModel
        fields = {'brand','model','vin','km','color','description','engine','transmission','image'}
