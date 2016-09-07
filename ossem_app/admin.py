from django.contrib import admin
from .models import (Manufacturer,
                     Model_,
                     Device,
                     Site,
                     Room,
                     Rack,
                     Bench,
                     Shelf,
                     Location)


# Register your models here.
@admin.register(Manufacturer)
class ManufacturerModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Model_)
class Model_ModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Device)
class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'location')


# admin.site.register(Manufacturer, ManufacturerModelAdmin)
# admin.site.register(Model_, Model_ModelAdmin)
# admin.site.register(Device, DeviceModelAdmin)
admin.site.register(Site)
admin.site.register(Room)
admin.site.register(Rack)
admin.site.register(Bench)
admin.site.register(Shelf)
admin.site.register(Location)