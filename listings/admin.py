from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','is_published', 'price', 'list_date', 'relators' )
    list_display_links = ('id', 'title')
    # list_filter = ('relators')
    list_editable = ('is_published',)
    search_fields = ('title', 'city', 'state', 'zipcode',)

admin.site.register(Listing, ListingAdmin)
 