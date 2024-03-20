
from django.contrib import admin
from .models import Farmer, Crop, PriceRecord

# Register your models here
admin.site.register(Farmer)
admin.site.register(Crop)
admin.site.register(PriceRecord)

# Explanation:
# We import the models and the admin.site object from Django.
# We use admin.site.register to register each model with the admin interface. 
# This allows us to create, edit, and delete data for these models through the admin interface.
