from curs.serializers import BaseCategoryserializers, CategorySerializers
from curs.models import BaseCategory, Category
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class CategoryListView(ListCreateAPIView):
    lookup_field = 'slug'
    queryset = Category
    serializer_class = CategorySerializers
