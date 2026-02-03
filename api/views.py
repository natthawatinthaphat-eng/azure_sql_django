from django.shortcuts import render
from .serializers import StoreSerializer, ProductSerializer, UserSerializer
from .models import Store, Product, User
from rest_framework import generics, response, status
from rest_framework.views import APIView

# Create your views here.


class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = 'store_id'


class StoreDeleteAll(APIView):
    def get(self, request, *args, **kwargs):
        serializer = StoreSerializer(Store.objects.all(), many=True)
        return response.Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        Store.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer   
    lookup_field = 'id'

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_id'

class UserDeleteAll(APIView):
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(User.objects.all(), many=True)
        return response.Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        User.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
        
        