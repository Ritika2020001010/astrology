from django.contrib import admin
from astroapp.models import contact_form


class ContactFormAdmin(admin.ModelAdmin):
    # Specify the fields to be displayed in the list view
    list_display = ('name', 'lastname', 'subject', 'email', 'message')
admin.site.register(contact_form, ContactFormAdmin)