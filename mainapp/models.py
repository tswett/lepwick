from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models, transaction
from django.db.models import CheckConstraint, F, Q

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
    amount = models.BigIntegerField(validators=[MinValueValidator(0)], default=0)

    class Meta:
        constraints = [
            CheckConstraint(check=Q(amount__gte=0), name='amount_gte_0'),
        ]

    def __str__(self):
        username = self.inventory.user.username
        amount = self.amount
        unit = self.commodity.minor_unit_plural
        return f'{username}: {amount} {unit}'
    
    @staticmethod
    def give(inventory, commodity, quantity):
        UserHolding.objects.get_or_create(inventory=inventory, commodity=commodity)

        holding = UserHolding.objects.filter(inventory=inventory, commodity=commodity)
        holding.update(amount=F('amount') + quantity)

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

            UserHolding.give(parent_holding.inventory, self.result, parent_amount * self.quantity)

class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def execute_for(self, inventory):
        with transaction.atomic():
            for item in self.items.all():
                UserHolding.give(inventory, item.commodity, item.quantity)

class RecipeItem(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='items')
    commodity = models.ForeignKey(Commodity, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.recipe.name} produces {self.quantity} of {self.commodity.name}'
