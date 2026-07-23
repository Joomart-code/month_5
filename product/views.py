from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Avg

@api_view(['GET','POST'])
def category_list_create_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategorySerializer(categories, many=True).data

        return Response(data)
    elif request.method == 'POST':
        data = CategorySerializer(data=request.data)
           
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(
            data={'error': 'category not found!'},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        serialzer = CategorySerializer(category)
        return Response(serialzer.data)
    
    elif request.method =='PUT':
        serialzer = CategorySerializer(category, data=request.data)
        
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(
            {'massage': 'Category deleted'},
            status=status.HTTP_204_NO_CONTENT
        )
        
        
        
@api_view(['GET'])
def product_list_create_api_view(request):
    if request.method == 'GET':
        products = Product.objects.annotate(
            rating = Avg('reviews__stars')
        )
        data = ProductSerializer(products, many=True).data
        return Response(data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(
            data = {'error': 'product not found!'},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        data = ProductSerializer(product).data
        return Response(data)
    
    
    elif request.method =='PUT':
        serializer = ProductSerializer(product, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT   )


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(
            data = {'error':'review not found!'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == 'GET':
        serializer = ReviewSerializer(reviews).data
        return Response(serializer)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(reviews, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)