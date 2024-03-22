from django.urls import path
from rest_framework.routers import DefaultRouter

from inventory.views import ProductsViewSet

router = DefaultRouter()
router.register("", ProductsViewSet, basename="products")
urlpatterns = [] + router.urls
