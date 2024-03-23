from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from order.models import Order, OrderItem
from cart.models import CartItems, Cart
from django.db import transaction


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class PlacedOrderSerializer(ModelSerializer):
    cart = serializers.SlugRelatedField(queryset=Cart.objects.all(), slug_field='id', write_only=True)
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['total_amount', 'vendor', 'user']

    # used transaction atomic if the order is not created then the cart will not be deleted
    @transaction.atomic
    def create(self, validated_data):
        cart = validated_data.pop('cart')
        order = Order.objects.create(total_amount=cart.total_price, vendor=cart.vendor, user=cart.user)
        # add all the items in the cart to the order items
        for item in cart.cart_item.all():
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.total_price)
        # remove carts after creating the order
        self.delete_cart_items(cart)
        return order

    def delete_cart_items(self, cart):
        cart.delete()
        return True
