from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ListingModel, LikedListing
from .forms import ListingForm
from users.forms import LocationForm
from django.contrib import messages
from .filters import ListingFilter
from django.core.mail import send_mail

# Create your views here.

def main_view(request):
    return render(request,"views/main.html", {"name":"AutoMax"})

@login_required
def home_view(request):
    listings = ListingModel.objects.all()
    lisitng_filter = ListingFilter(request.GET, queryset=listings)
    user_liked_listings = LikedListing.objects.filter(profile = request.user.profile).values_list('listing')
    liked_listings_ids = [l[0]for l in user_liked_listings]
    context = {
        'listing_filter' : lisitng_filter,
        'liked_listings_ids': liked_listings_ids
    }
    #'listings': listings <- eso estaba dentro del contexto xq desde el home mostraba todos los autos dentro del for. Como ahora necesito aplicar filtros, los autos que voy a mostrar en el loop tienen que venir desde el objeto que los contiene filtrados
    return render(request, "views/home.html",context)

@login_required
def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            location_form = LocationForm(request.POST)
            if listing_form.is_valid() and location_form.is_valid():
                listing = listing_form.save(commit=False)
                listing_location = location_form.save()
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(request, f'{listing.model} agregado correctamente')
                return redirect('home')
            else:
                raise Exception()   
        except Exception as e:
            print(e)
            messages.error(request, 'Ocurrió un error durante la carga del formulario de tu auto')
    elif request.method == 'GET':
        listing_form = ListingForm()
        location_form = LocationForm()
    return render(request, 'views/list.html', {'listing_form': listing_form, 'location_form':location_form})

@login_required
def listing_view(request, id):
    try:
        listing = ListingModel.objects.get(id=id)
        if listing is None:
            raise Exception
        return render(request, 'views/listings.html',{'listing': listing})
    except Exception as e:
        messages.error(request, f'Invalid id {id}')
        return redirect('home')

@login_required 
def edit_view(request, id):
    try:
        listing = ListingModel.objects.get(id=id)
        if listing is None:
            raise Exception
        if request.method == 'POST':
            listing_form = ListingForm(request.POST, request.FILES, instance=listing)
            location_form = LocationForm(request.POST, instance=listing.location)
            if listing_form.is_valid and location_form.is_valid:
                listing_form.save()
                location_form.save()
                messages.info(request, f'Los datos fueron actualizados correctamente')
                return redirect('home')
            else:
                messages.error(request, f'Ocurrió un error en la edición')
                raise Exception
        else:
            listing_form = ListingForm(instance=listing)
            location_form = LocationForm(instance=listing.location)
        context = {
            'listing_form': listing_form,
            'location_form': location_form
        }
        return render(request, 'views/edit.html', context)
    except Exception as e:
        messages.error(request, f'Ocurrió un error en la edición')
        return redirect('home')

@login_required 
def like_listing_view(request, id):
    
    listing = get_object_or_404(ListingModel, id=id)
    liked_listing, created = LikedListing.objects.get_or_create(profile=request.user.profile, listing = listing)
    if not created:
        liked_listing.delete()
    else:
        liked_listing.save()
    
    return JsonResponse({
        'is_liked_by_user': created,
    })

def inquire_listing_using_email(request, id):
    listing = get_object_or_404(ListingModel, id=id)
    try:
        emailSubject = f'{request.user.username} le interesa {listing.model}'
        emailMessage= f'Hola, {listing.seller.user.username}, al usuario {request.user.username} le interesa {listing.model}'
        send_mail(emailSubject, emailMessage, request.user.email, [listing.seller.user.email,], fail_silently=True)
        return JsonResponse({
          'success': True 
        })
    except Exception as e:
        print(e)
        return JsonResponse({
            'success': False,
            'info': e
        })