from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    """Serializes a name field for testing TestApiView"""

    name = serializers.CharField(max_length=5)
