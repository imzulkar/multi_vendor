from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
USER_TYPE = (
    ('BUYER', 'Buyer'),
    ('SELLER', 'Seller'),
)


class User(AbstractUser):
    user_type = models.CharField(choices=USER_TYPE, max_length=10, default='BUYER')

    def __str__(self):
        return self.user_type
