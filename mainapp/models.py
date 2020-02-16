from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import F

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

class CommodityOutput(models.Model):
    parent = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    result = models.ForeignKey(Commodity, on_delete=models.CASCADE,
        related_name='commodity_output_parent')
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.parent.name} produces {self.quantity} of {self.result.name}'
    
    def produce(self):
        parent_holdings = UserHolding.objects.filter(commodity=self.parent)

        for parent_holding in parent_holdings:
            parent_amount = parent_holding.amount

            #result_holding, created = UserHolding.objects.get_or_create(
            #    inventory=parent_holding.inventory, commodity=self.result)

            #result_holding.update(amount=F('amount') + parent_amount * self.quantity)

            UserHolding.objects.update_or_create(
                inventory=parent_holding.inventory, commodity=self.result,
                defaults={'amount': F('amount') + parent_amount * self.quantity}
            )
