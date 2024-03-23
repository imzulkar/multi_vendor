from django.urls import path

from shop.views import index_view, product_list, cart_views

app_name = 'shop'
urlpatterns = [

    path("", index_view, name="index_template"),
    path("cart/", cart_views, name="cart_template"),
    path("products/", product_list, name="products_list_template"),
]
