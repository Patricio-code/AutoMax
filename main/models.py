from django.db import models
import uuid
from users.models import Profile, Locations
from .consts import CAR_BRAND, TRANSMISSION_OPTIONS
from .utils import user_listing_path
# Create your models here.
class ListingModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    brand = models.CharField(max_length=24, choices=CAR_BRAND, default=None)
    model = models.CharField(max_length=64,default='')
    vin = models.CharField(max_length=6, default='')
    km = models.IntegerField(default=0)
    color = models.CharField(max_length=24, default='')
    description = models.TextField(default='')
    engine = models.CharField(max_length=24, default='')
    transmission = models.CharField(max_length=24, choices = TRANSMISSION_OPTIONS, default=None)
    location = models.OneToOneField(Locations, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=user_listing_path, null=True)

    def __str__(self):
        return f'{self.seller.user.username}\'s Listing -  {self.model}'

class LikedListing(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    listing = models.ForeignKey(ListingModel, on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.listing.model} likeado por {self.profile.user.username}'
