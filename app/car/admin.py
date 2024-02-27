from django.contrib import admin

from car.models import Car, Owner


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'license_plate', 'brand', 'year')
    fields = ('license_plate', 'brand', 'year', 'color', 'condition', 'owner')
    readonly_fields = ('id', )
    ordering = ('id',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    fields = (('first_name', 'last_name'), ('sex', 'date_of_birth'), 'address')
    readonly_fields = ('id',)
