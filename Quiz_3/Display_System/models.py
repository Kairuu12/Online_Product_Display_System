from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()

    def product_info(self):
        return f"{self.name} costs {int(self.price) if float(self.price).is_integer() else self.price}"

    def __str__(self):
        return self.name
