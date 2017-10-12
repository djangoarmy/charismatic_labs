from django.contrib import admin
from .models import ContactDetails

class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email')
    fieldsets = (
        ('', {'fields': (
            'contact_name',
            'contact_email',
            'contact_subject',
            'contact_message',
        )}),
    )

admin.site.register(ContactDetails, ContactDetailsAdmin)