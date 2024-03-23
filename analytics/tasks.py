from __future__ import absolute_import, unicode_literals

from datetime import datetime, timedelta
from celery import Celery
from django.db import transaction
from django.db.models import Sum

from analytics.models import DailyOrderSummary
from vendor.models import Vendor

app = Celery()


@app.task
def calculate_daily_order_summary(date=datetime.today().date() - timedelta(days=1)):
    vendors = Vendor.objects.prefetch_related('orders_vendors')
    for vendor in vendors:
        with transaction.atomic():
            orders = vendor.orders_vendors.filter(created_at__date=date)
            if orders.exists():
                order = orders.aggregate(total=Sum('total_amount'))
                if DailyOrderSummary.objects.filter(date=date, vendor=vendor).exists():
                    daily_order_summary = DailyOrderSummary.objects.get(date=date, vendor=vendor)
                    daily_order_summary.total_amount = float(order['total'])
                    daily_order_summary.save()
                summary = DailyOrderSummary.objects.create(date=date, vendor=vendor, total_amount=float(order['total']))
