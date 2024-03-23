from django.urls import path

from shop.views import index_view, product_list, cart_views, my_cart_views

app_name = 'shop'
urlpatterns = [

    path("", index_view, name="index_template"),
    path("cart/", cart_views, name="cart_template"),
    path("my-cart/", my_cart_views, name="my_cart_template"),
    path("products/", product_list, name="products_list_template"),
]
