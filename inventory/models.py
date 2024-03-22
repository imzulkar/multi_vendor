from django.db import models
from config.base_model import BaseModel
from vendor.models import Vendor


# Create your models here.

class Products(BaseModel):
    """this is an inventory model that stores the product details of a vendor"""
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor_product')
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='product_image', blank=True)
    description = models.TextField(blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
