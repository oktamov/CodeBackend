from rest_framework.response import Response

from curs.serializers import BaseCategoryserializers, CategorySerializers
from curs.models import BaseCategory, Category
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


# class CategoryListView(APIView):
#     def get(self, request, slug):
#         products = Category.objects.filter(basecategory__slug=slug)
#         serializer = CategorySerializers(products, many=True)
#         return Response(serializer.data)

class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category
    serializer_class = CategorySerializers
    lookup_field = 'slug'
