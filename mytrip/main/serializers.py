from rest_framework import serializers
from .models import barrier_free_hotel, categorized

# JSON 데이터 형태로 렌더링하기

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = barrier_free_hotel
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categorized
        fields = '__all__'

