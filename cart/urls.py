from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CartViewSet

router = DefaultRouter()
router.register("", CartViewSet, basename="carts")
urlpatterns = [
                  path("add/", CartViewSet.as_view({"post": "add_to_cart"}), name="add_to_cart"),
              ] + router.urls
