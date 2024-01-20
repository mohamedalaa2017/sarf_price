from rest_framework import serializers

from .models import Currency_Prices, Gold, Post

class CurrencyPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency_Prices
        fields = '__all__'
        depth = 2


class GoldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gold
        fields = '__all__'
        depth = 2


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'