from order.serializers import PlacedOrderSerializer
from order.models import Order
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PlaceOrderView(ModelViewSet):
    queryset = Order.objects.prefetch_related('order_items')
    serializer_class = PlacedOrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.user_type == 'SELLER':
                return self.queryset.filter(vendor=self.request.user.vendor_user)
        return self.queryset.filter(user=self.request.user)
