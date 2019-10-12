from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

class Commodity(models.Model):
    name = models.CharField(max_length=50)
    minor_unit_plural = models.CharField('minor unit (plural)', max_length=50)

    def __str__(self):
        return self.name

class UserInventory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contents = models.ManyToManyField(Commodity, through='UserHolding')

    def __str__(self):
        return self.user.username

class UserHolding(models.Model):
    inventory = models.ForeignKey(UserInventory, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    amount = models.BigIntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        username = self.inventory.user.username
        amount = self.amount
        unit = self.commodity.minor_unit_plural
        return f'{username}: {amount} {unit}'
