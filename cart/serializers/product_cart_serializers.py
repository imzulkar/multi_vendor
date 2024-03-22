from rest_framework.serializers import ModelSerializer
from cart.models import Cart, CartItems


class CartItemsSerializer(ModelSerializer):
    class Meta:
        model = CartItems
        fields = "__all__"


class CartSerializer(ModelSerializer):
    cart_item = CartItemsSerializer(many=True)

    class Meta:
        model = Cart
        fields = "__all__"

    def create(self, validated_data):
        # created the cart item data from the validated data
        cart_item_data = validated_data.pop('cart_item')
        cart = Cart.objects.create(**validated_data)
        for item in cart_item_data:
            CartItems.objects.create(cart=cart, **item)
        return cart
