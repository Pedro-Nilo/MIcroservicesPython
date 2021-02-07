from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, User
from .serializers import ProductSerializer

import random


class ProductViewSet(viewsets.ViewSet):
    # /api/products GET
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    # /api/products POST
    def create(self, request):
        serializer = ProductSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # /api/products/<str:pk> GET
    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)

        return Response(serializer.data)

    # /api/products/<str:pk> PATCH
    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # /api/products/<str:pk> DELETE
    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)

        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserApiView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)

        return Response({
            'id': user.id
        })
