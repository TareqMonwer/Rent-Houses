from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Listing
from listings.choices import (price_choices,
                              bedroom_choices,
                              state_choices)



def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    pagination = Paginator(listings, 2)
    page = request.GET.get('page')
    paged_listings = pagination.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = { 'listing': listing}
    return render(request, 'listings/listing.html', context)


def search(request):
    listings_qs = Listing.objects.none()
    # getting cities where at-least one listing presents.
    active_cities = Listing.objects.order_by().values_list('city').distinct()
    active_cities = [x[0] for x in active_cities]
    # getting search result from 'keywords'
    if 'keywords' in request.GET:
        keywords = request.GET.get('keywords')
        listings_qs = Listing.objects.filter(description__icontains=keywords)
    # getting search result from 'city'
    if 'city' in request.GET:
        city = request.GET.get('city')
        listings_qs = Listing.objects.filter(city__iexact=city)
    # getting search result from 'state'
    if 'state' in request.GET:
        state = request.GET.get('state')
        listings_qs = Listing.objects.filter(state__iexact=state)
    # getting search result from 'bedrooms'
    if 'bedrooms' in request.GET:
        bedrooms = request.GET.get('bedrooms')
        listings_qs = Listing.objects.filter(bedrooms__lte=bedrooms)
    # getting search result from 'price'
    if 'price' in request.GET:
        price = request.GET.get('price')
        listings_qs = Listing.objects.filter(price__lte=price)
    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': listings_qs, 
        'active_cities': active_cities,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
