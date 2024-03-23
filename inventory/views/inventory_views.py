from rest_framework.viewsets import ModelViewSet
from inventory.models import Products
from inventory.serializers import ProductsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.user_type == 'SELLER':
                return self.queryset.filter(vendor=self.request.user.vendor_user)
        return self.queryset
