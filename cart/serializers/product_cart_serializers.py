from django.db import transaction
from django.db.models import Sum, Count
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from cart.models import Cart, CartItems
from inventory.models import Products
from user.models import User
from utils.helper import cart_price_calculator
from vendor.models import Vendor


class CartProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'image']


class CartItemsSerializer(ModelSerializer):
    product = CartProductsSerializer(read_only=True)

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
            total_price = cart_price_calculator(product.price, quantity)
            grand_total += total_price
            total_items += quantity
            bulk_object.append(CartItems(cart=cart, product=product, quantity=quantity, total_price=total_price))
        CartItems.objects.bulk_create(bulk_object)

        # update the cart total price and quantity
        cart.total_price = grand_total
        cart.quantity = total_items

        cart.save(update_fields=['total_price', 'quantity'])
        return cart


class AddToCartSerializer(serializers.Serializer):
    vendor = serializers.SlugRelatedField(slug_field='id', queryset=Vendor.objects.all())
    product = serializers.SlugRelatedField(slug_field='id', queryset=Products.objects.all())
    quantity = serializers.IntegerField()

    def create(self, validated_data):

        vendor = validated_data.get('vendor')
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')
        # calculate the total price of the product
        total_price = cart_price_calculator(product.price, quantity)
        request = self.context.get('request')
        cart = Cart.objects.filter(user=request.user, vendor=vendor)
        # check if the cart exists
        if cart.exists():
            cart = cart.first()
        else:
            cart = Cart.objects.create(user=request.user, vendor=vendor)
        cart_item = CartItems.objects.create(cart=cart, product=product, quantity=quantity, total_price=total_price)
        total = CartItems.objects.filter(cart=cart).aggregate(total=Sum('total_price'), item=Count('product'))
        cart.total_price = total['total']
        cart.quantity = total['item']
        cart.save(update_fields=['total_price', 'quantity'])
        return cart_item
