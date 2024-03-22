from rest_framework.viewsets import ModelViewSet
from inventory.models import Products
from inventory.serializers import ProductsSerializer


class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
