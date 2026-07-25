from rest_framework import serializers
from .models import Category, Product, Review
from rest_framework.exceptions import ValidationError

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = '__all__'
    def get_products_count(self, obj):
        return obj.products.count()
    
    def validate_name(self,value):
        if len(value) < 3 or len(value)>100:
            raise serializers.ValidationError(
                'Name must be between 3 and 100 characters'
                )
        exists = Category.objects.filter(name=value).exists()
        
        if exists:
            raise serializers.ValidationError(
                'Category already exists'
                )
        
        return value
    
    
        
class ProductSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        
    def validate_title(self, value):
        value = value.strip()
        
        if len(value)<3:
            raise serializers.ValidationError(
            'The title cannot be less than 3 characters!'
                )
        return value
    
    def validate_price(self, value):
        if value<=0:
            raise serializers.ValidationError(
            'The price cannot be less than zero!'
                )
        return value
    
    def validate_description(self, value):
        if len(value.strip())<10:
            raise serializers.ValidationError(
            'Description must contain at least 10 characters'
            )
        return value
        

        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
    
    
    def validate_text(self,value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError(
            'The text must contain at least 5 characters'
            )
        return value
    
    
    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
            'The number must be between 1 and 5'
            )
        return value