from rest_framework import serializers
from api.models import Flower, Manager
class FlowerSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = 'id','name','price','description','image','light','temp','humidity','watering','fertilizer','transplantatio'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flower
        fields = 'id','username','password'

class ShippingSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone = serializers.CharField()
    flower = FlowerSerilizer()

class CommentSerializer(serializers.Serializer):
    name = serializers.CharField()
    text = serializers.CharField()
    flower = FlowerSerilizer()
    