from rest_framework.viewsets import ModelViewSet
from cart.models import Cart, CartItems
from cart.serializers import CartSerializer, CartItemsSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.prefetch_related('cart_item')
    serializer_class = CartSerializer

    def get_queryset(self):
        # if the user is authenticated and the user is a seller then return the cart of the seller or return the cart of the user
        # print(self.request.user.vendor_user)
        if self.request.user.is_authenticated:
            if self.request.user.user_type == 'SELLER':
                return Cart.objects.filter(vendor=self.request.user.vendor_user)
            return Cart.objects.filter(user=self.request.user)
