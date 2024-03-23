from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("", include("shop.urls")),
                  path("user/", include("user.urls")),
                  path("api/vendor/", include("vendor.urls")),
                  path("api/inventory/", include("inventory.urls")),
                  path("api/cart/", include("cart.urls")),
                  path("api/order/", include("order.urls")),
                  path("api/annalytics/", include("analytics.urls")),
              ] + [
                  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
              ] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
