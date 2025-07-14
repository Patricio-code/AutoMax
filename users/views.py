from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.utils.decorators import method_decorator
from .forms import UserForm, ProfileForm, LocationForm
from main.models import ListingModel, LikedListing
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username= username,password= password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Estás logueado como {user.username}')
                return redirect('home') # o redirect(settings.LOGIN_REDIRECT_URL) importando from proyecto import settings, teniendo en LOGIN_REDIRECT_URL = '/home/'
            else: 
                messages.error(request, f'Ocurrió un error intentado loguearte')
        else:
            messages.error(request, f'Ocurrió un error intentado loguearte')
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request, 'views/login.html', {'login_form': login_form})

"""def register_view(request):
    register_form = UserCreationForm()
    return render(request, 'views/register.html', {'register_form': register_form})"""

@login_required
def logout_view(request):
    logout(request)
    return redirect('main')


class RegisterView(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'views/register.html',{'register_form': register_form})
    
    def post(self,request):
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            login(request,user)
            messages.success(request, f'Estás registrado como {user.username}')
            return redirect('home') # o redirect(settings.LOGIN_REDIRECT_URL) importando from proyecto import settings, teniendo en LOGIN_REDIRECT_URL = '/home/'
        else:
            messages.error(request, f'Ocurrió un error intentado registrarte')
            return render(request, 'views/register.html',{'register_form': register_form})

@method_decorator(login_required, name='dispatch')
class ProfileView(View):

    def get(self, request):
        user_listings = ListingModel.objects.filter(seller=request.user.profile)
        user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).all()
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        location_form = LocationForm(instance=request.user.profile.location)
        return render(request, 'views/profile.html',{'user_form': user_form, 'profile_form':profile_form, 'location_form':location_form, 'user_listings': user_listings, 'user_liked_listings':user_liked_listings,})
    
    def post(self,request):
        user_listings = ListingModel.objects.filter(seller=request.user.profile)
        user_liked_listings = LikedListing.objects.filter(profile=request.user.profile).all()
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        location_form = LocationForm(request.POST, instance=request.user.profile.location)

        if user_form.is_valid() and profile_form.is_valid() and location_form.is_valid():
            user_form.save()
            profile_form.save()
            location_form.save()
            messages.success(request, 'Perfil actualizado')
            return redirect('profile')
        else:
            messages.error(request, 'Error al actualizar el perfil')
        
        return render(request, 'views/profile.html',{'user_form': user_form, 'profile_form':profile_form, 'location_form':location_form, 'user_listings': user_listings, 'user_liked_listings':user_liked_listings,})