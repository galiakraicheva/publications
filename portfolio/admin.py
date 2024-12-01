from django.contrib import admin
from .models import Publication

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    fields = ('title', 'description', 'link', 'file')  # Order of fields in the form

admin.site.register(Publication, PublicationAdmin)