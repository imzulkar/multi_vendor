from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from cart.models import Cart, CartItems
from cart.serializers import CartSerializer, CartItemsSerializer, AddToCartSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.prefetch_related('cart_item__product').select_related('vendor')
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'add_to_cart':
            return AddToCartSerializer
        return self.serializer_class

    def get_queryset(self):
        # if the user is authenticated and the user is a seller then return the cart of the seller or return the cart of the user
        # print(self.request.user.vendor_user)
        if self.request.user.is_authenticated:
            if self.request.user.user_type == 'SELLER':
                return Cart.objects.filter(vendor=self.request.user.vendor_user)
            return Cart.objects.filter(user=self.request.user)

    def add_to_cart(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Product added to cart successfully!'}, status=status.HTTP_201_CREATED)
