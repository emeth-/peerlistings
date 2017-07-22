from django.contrib import admin

from api.models import Listing
class ListingAdmin(admin.ModelAdmin):
    list_display = ('tx_id', 'seller_address')
    search_fields = ('tx_id',)
admin.site.register(Listing, ListingAdmin)
