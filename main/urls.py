from django.urls import path
from .views import main_view, home_view, list_view,listing_view, edit_view, like_listing_view, inquire_listing_using_email# , login_link

urlpatterns = [
    path('',main_view, name = 'main'),
    path('home/', home_view, name='home'),
    path('list/',list_view, name='list'),
    path('listings/<str:id>',listing_view,name='listings'),
    path('listings/<str:id>/edit', edit_view, name="edit"),
    path('listings/<str:id>/like/',like_listing_view , name="like_listing"),
    path('listings/<str:id>/inquire/',inquire_listing_using_email , name="inquire_listing"),
]

#path('login/', login_link, name='login_link'),
