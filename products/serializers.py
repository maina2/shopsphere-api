from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()  # Shows category name instead of ID
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())  # Allow category ID
    image = serializers.SerializerMethodField()  # Add this line

    class Meta:
        model = Product
        fields = '__all__'

    def get_image(self, obj):
        if obj.image:
            # Construct the full Cloudinary URL
            return f"https://res.cloudinary.com/duknvsch4/{obj.image}"
        return None


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()  # Add this line

    class Meta:
        model = Category
        fields = '__all__'

    def get_image(self, obj):
        if obj.image:
            # Construct the full Cloudinary URL
            return f"https://res.cloudinary.com/duknvsch4/{obj.image}"
        return None
