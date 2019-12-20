from django.shortcuts import render
from listings.models import Listing, Realtor
from listings.choices import (price_choices,
                             bedroom_choices,
                             state_choices)

def index(request):
    latest_listings = Listing.objects.order_by('-is_published').filter(is_published=True)[:3]
    context = {
        'listings': latest_listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp = list(Realtor.objects.filter(is_mvp=True).order_by('-last_updated'))[-1]
    print(mvp)
    context = {
        'team': realtors,
        'mvp': mvp
    }
    return render(request, 'pages/about.html', context)
