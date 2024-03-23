from django.urls import path
from order.views import PlaceOrderView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api', PlaceOrderView, basename='order')
urlpatterns = [] + router.urls
