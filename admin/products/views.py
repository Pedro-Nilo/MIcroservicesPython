from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    # /api/products GET
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    # /api/products POST
    def create(self, request):
        pass

    # /api/products/<str:pk> GET
    def retrieve(self, request, pk=None):
        pass

    # /api/products/<str:pk> PATCH
    def update(self, request, pk=None):
        pass

    # /api/products/<str:pk> DELETE
    def destroy(self, request, pk=None):
        pass
