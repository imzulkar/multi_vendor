from django.db import models

# Create your models here.
from user.models import User
from vendor.models import Vendor
from inventory.models import Products
from config.base_model import BaseModel


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_user')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,
                               related_name='orders_vendors')  # Associate each item with its vendor

    def __str__(self):
        return self.vendor.name


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField(default=0.0)  # Store the price at the time of purchase

    def __str__(self):
        return self.product.name
