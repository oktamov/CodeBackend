from rest_framework import serializers
from .models import *


class BaseCategoryserializers(serializers.ModelSerializer):
    class Meta:
        model = BaseCategory
        fields = ["id", "name", "slug"]


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]
