from django.shortcuts import render
from rest_framework.views import APIView, Response

from product.models import Product
from product.serializers import ProductSerializer


class ProductView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
