from config.base_model import BaseModel
from django.db import models
from user.models import User


# Create your models here.
class Vendor(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendor_user')
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=30, blank=True)
    logo = models.ImageField(upload_to='vendor_logo', blank=True)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name
