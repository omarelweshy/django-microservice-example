from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=225)
    product_price = models.CharField(max_length=225)
