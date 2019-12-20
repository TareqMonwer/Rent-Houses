from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price',
                    'is_published', 'realtor', 'city')
    list_display_links = ('id', 'title')
    list_editable = ('is_published', )
    list_filter = ('realtor', 'city')
    search_fields = ['realtor__name', 'title', 'city', 'zip_code', 'price', 'sqr_ft']
    list_per_page = 30


admin.site.register(Listing, ListingAdmin)
