"""Serializer for the restAPIApp"""

# ? Serializer is used to convert complex data types, such as Django models, into JSON format that can be easily
# ? rendered into a response. It also provides deserialization, allowing parsed data to be converted back into complex
# ? types after being validated.

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'