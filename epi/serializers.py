# api/serializers.py

from epi.models import *
from rest_framework import serializers

class Data3InlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = 'name', 'county','size', 'weight', 'children'

class Data2InlineSerializer(serializers.ModelSerializer):
    children = Data3InlineSerializer(many=True, read_only=True)
    class Meta:
        model = Data
        fields = 'name', 'county','size', 'weight', 'children'

class Data1InlineSerializer(serializers.ModelSerializer):
    children = Data2InlineSerializer(many=True, read_only=True)
    class Meta:
        model = Data
        fields = 'name', 'county','size', 'weight', 'children'

class DataInlineSerializer(serializers.ModelSerializer):
    children = Data1InlineSerializer(many=True, read_only=True)
    class Meta:
        model = Data
        fields = 'name', 'county','size', 'weight', 'children'

class DataSerializer(serializers.ModelSerializer):
    children = DataInlineSerializer(many=True, read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Data
        fields = ('name', 'county','size', 'weight', 'children')

class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Data
        fields = ('__all__')
        read_only_fields = ('date_created', 'date_modified')