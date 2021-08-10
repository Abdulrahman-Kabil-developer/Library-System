from rest_framework import serializers
from .models import book


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model=book
        fields='__all__'