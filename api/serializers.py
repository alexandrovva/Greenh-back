from rest_framework import serializers

class FlowerSerilizer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.FloatField()
    description = serializers.CharField()
    image = serializers.CharField()
    light = serializers.CharField()
    temp = serializers.CharField()
    humidity = serializers.CharField()
    watering = serializers.CharField()
    fertilizer = serializers.CharField()
    transplantatio = serializers.CharField()
    id = serializers.IntegerField(required=False)