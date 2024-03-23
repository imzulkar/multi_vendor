from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

import vendor.urls

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("", include("user.urls")),
                  path("vendor/", include("vendor.urls")),
                  path("inventory/", include("inventory.urls")),
                  path("cart/", include("cart.urls")),
                  path("order/", include("order.urls")),
                  path("annalytics/", include("analytics.urls")),
              ] + [
                  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
              ] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
