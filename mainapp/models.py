from django.db import models

class Commodity(models.Model):
    name = models.CharField(max_length=50)
    minor_unit_plural = models.CharField('minor unit (plural)', max_length=50)

    def __str__(self):
        return self.name
