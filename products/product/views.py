from rest_framework.views import APIView, Response

from product.models import Product
from product.serializers import ProductSerializer
from product.decorators import validate_user_token


class ProductView(APIView):
    @validate_user_token
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
