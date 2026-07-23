from rest_framework import serializers
from .models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'
    def get_products_count(self, obj):
        return count.products.count()
        
class ProductSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
    