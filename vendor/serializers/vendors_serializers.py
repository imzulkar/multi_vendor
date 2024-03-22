from rest_framework.serializers import ModelSerializer
from inventory.models import Vendor


class VendorSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"
