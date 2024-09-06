from rest_framework import serializers
from .models import Weather, Crop, Region, CropCoefficient, Province

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'  # Include all fields

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'  # Include all fields

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'  # Include all fields

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'  # Include all fields

class CropCoefficientSerializer(serializers.ModelSerializer):
    crop = CropSerializer()  # Nested serializer for crop data
    province = ProvinceSerializer()  # Nested serializer for province data

    class Meta:
        model = CropCoefficient
        fields = ('id', 'crop', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'province', 'created_at')
