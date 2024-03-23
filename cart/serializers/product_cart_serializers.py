from django.db import transaction
from rest_framework.serializers import ModelSerializer
from cart.models import Cart, CartItems
from utils.helper import cart_price_calculator


class CartItemsSerializer(ModelSerializer):
    class Meta:
        model = CartItems
        fields = "__all__"
        read_only_fields = ["cart", "total_price"]


class CartSerializer(ModelSerializer):
    cart_item = CartItemsSerializer(many=True)

    class Meta:
        model = Cart
        fields = "__all__"
        read_only_fields = ["total_price", "quantity", "user"]

    @transaction.atomic
    def create(self, validated_data):
        # created the cart item data from the validated data
        cart_item_data = validated_data.pop('cart_item')
        cart = Cart.objects.create(**validated_data)
        grand_total = 0
        total_items = 0
        bulk_object = []

        # loop through the cart item data and create the cart item
        for item in cart_item_data:
            product = item.pop('product')
            quantity = item.pop('quantity')
            # product price calculator
            total_price = cart_price_calculator(product, quantity)
            grand_total += total_price
            total_items += quantity
            bulk_object.append(CartItems(cart=cart, product=product, quantity=quantity, total_price=total_price))
        CartItems.objects.bulk_create(bulk_object)

        # update the cart total price and quantity
        cart.total_price = grand_total
        cart.quantity = total_items

        cart.save(update_fields=['total_price', 'quantity'])
        return cart
