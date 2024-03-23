from django.urls import path
from rest_framework.routers import DefaultRouter

from inventory.views import ProductsViewSet
from inventory.views.product_list_views import product_list

router = DefaultRouter()
router.register("api/products", ProductsViewSet, basename="products")

app_name = "inventory"
urlpatterns = [
                  path("products", product_list, name="products_list_template"),
              ] + router.urls
