from django.contrib import admin
from .models import Bus, Ticket

# Register your models here.
@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'departure_time', 'available_seats', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'number')
    prepopulated_fields = {'slug': ('title', 'number')}
    ordering = ('status', 'available_seats')

@admin.register(Ticket)
class BusAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'booked_seats', 'bus')
    list_filter = ('bus',)
    search_fields = ('name', 'number')
    prepopulated_fields = {'slug': ('name', 'number')}
    ordering = ('booked_seats',)