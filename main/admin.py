from django.contrib import admin
from .models import ListingModel, LikedListing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description') # esto lo puedo usar para customizar la vista del admin sobre el modelo
    readonly_fields = ('id','vin' )

class LikedListingAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description') # esto lo puedo usar para customizar la vista del admin sobre el modelo

admin.site.register(ListingModel, ListingAdmin)
admin.site.register(LikedListing, LikedListingAdmin)