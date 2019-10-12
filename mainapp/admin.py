from django.contrib import admin

from .models import Commodity, UserHolding, UserInventory

admin.site.register(Commodity)
admin.site.register(UserHolding)
admin.site.register(UserInventory)
