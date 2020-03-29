from django.contrib import admin

from . import models

admin.site.register(models.Commodity)
admin.site.register(models.UserHolding)
admin.site.register(models.UserInventory)
admin.site.register(models.CommodityOutput)
admin.site.register(models.Recipe)
admin.site.register(models.RecipeItem)
