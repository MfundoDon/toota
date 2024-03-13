from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import User, Driver, Trip 

# Register your models here.
admin.site.site_header = 'Toota Admin'
admin.site.site_title = 'Toota Admin Area'
admin.site.index_title = 'Welcome to Toota Admin Area'
@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    
    list_display = ('id','email', 'full_name', 'phone_number', 'is_staff', 'is_active', 'created', 'updated', 'is_verified')
    ordering = ('full_name',)
    


@admin.register(Driver)
class DriverAdmin(DefaultUserAdmin):
    list_display = ('id', 'email', 'full_name', 'phone_number', 'physical_address', 'vehicle_registration', 'vehicle_type', 'licence_no' )
    ordering = ('full_name',)
    



@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    fields = (
        'id', 
        'pickup_location', 
        'dropoff_location', 
        'driver',
        'user',
        'vehicle_type', 
        'pickup_time',
        'load_description',
        'status',
        'created',
        'updated', 
        'rating',
        'bid'
    )
    list_display = (
        'id', 
        'pickup_location', 
        'dropoff_location', 
        'driver',
        'user',
        'vehicle_type', 
        'pickup_time', 
        'load_description',
        'status',
        'created',
        'updated', 
        'rating',
        'bid'
    
    )
    
    list_filter = (
        'status',
    )
    
    readonly_fields = (
        'id', 'created', 'updated'
    
    )

