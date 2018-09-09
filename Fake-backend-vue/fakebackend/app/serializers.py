from .models import Customer
from rest_framework import serializers


class CustumerSerializer(serializers.ModelSerializer):
    """Serializes an Address object"""

    class Meta:
        model = Customer
        fields = "__all__"