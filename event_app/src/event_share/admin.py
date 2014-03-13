from django.contrib import admin

# Register your models here.
from .models import Event

class EventsAdmin(admin.ModelAdmin):
    class Meta:
        model = Event

admin.site.register(Event, EventsAdmin)