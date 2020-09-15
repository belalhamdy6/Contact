from django.contrib import admin
from .models import Contact
from django.contrib.auth.models import Group


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'info', 'gender')
    search_fields = ('name', 'email', 'phone', 'info', 'gender')
    list_filter = ('gender', 'date_added')

admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)