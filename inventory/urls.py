from rest_framework.routers import DefaultRouter

from inventory.views import ProductsViewSet

router = DefaultRouter()
router.register("products", ProductsViewSet, basename="products")

app_name = "inventory"
urlpatterns = [
              ] + router.urls
