from django.db import models
from config.base_model import BaseModel
from order.models import Order
from vendor.models import Vendor


class DailyOrderSummary(BaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='daily_order_summary')
    date = models.DateField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.vendor.name
