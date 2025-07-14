import django_filters
from .models import ListingModel

class ListingFilter(django_filters.FilterSet):
    
    class Meta:
        model = ListingModel
        fields = {'brand': {'exact'},'transmission': {'exact'}, 'km': {'lt','gt'},'model':{'icontains'}}