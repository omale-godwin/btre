from django.contrib import admin

# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display_links = ('id', 'name')
    list_display = ('id', 'name', 'email', 'phone', 'message')
    search_fields = ('name', 'listing', 'email')




admin.site.register(Contact, ContactAdmin)