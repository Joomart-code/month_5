from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Avg
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class CatrgoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
    
        
class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.annotate(
            rating = Avg('reviews__stars')
        )

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    
class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
    
class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'