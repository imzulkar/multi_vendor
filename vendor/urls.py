from rest_framework.routers import DefaultRouter

from vendor.views import VendorViewSet

router = DefaultRouter()
router.register(r'', VendorViewSet, basename='vendors')
urlpatterns = [] + router.urls
