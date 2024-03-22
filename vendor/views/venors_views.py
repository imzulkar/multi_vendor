from rest_framework.viewsets import ModelViewSet
from inventory.models import Vendor
from vendor.serializers import VendorSerializer


class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
