from django.db import models
from config.base_model import BaseModel
from inventory.models import Products
from vendor.models import Vendor
from user.models import User


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cart')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor_cart')
    quantity = models.IntegerField(default=0)
    total_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.vendor.name


class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_cart')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.product.name
