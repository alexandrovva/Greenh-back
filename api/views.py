from django.shortcuts import render
from api.models import Flower, Shipping, Comment
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from api.serializers import FlowerSerilizer, ShippingSerializer, CommentSerializer
from rest_framework.views import status, APIView
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
def flower_list(request):
    if request.method == 'GET':
        try:
            flowers = Flower.objects.all()
            serializer = FlowerSerilizer(flowers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    if request.method == 'POST':
        flower = Flower.objects.create(
            name = request.data['name'],
            price = request.data['price'],
            description = request.data['description'],
            image = request.data['image'],
            light = request.data['light'],
            temp = request.data['temp'],
            humidity = request.data['humidity'],
            watering = request.data['watering'],
            fertilizer = request.data['fertilizer'],
            transplantatio = request.data['transplantatio'],
        )

        return Response({"flower":"atbbe"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def flower_detailed(request, flower_id):
    try:
        flower = Flower.objects.get(id=flower_id)
    except:
        return Response({"": ""}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    if request.method == 'GET':
            serializer = FlowerSerilizer(flower)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
@permission_classes(IsAuthenticated, )    
@api_view(['PUT', 'DELETE'])
def flower_admin(request, flower_id):
    try:
        flower = Flower.objects.get(id=flower_id)
    except:
        return Response({"": ""}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if request.method =='PUT':
        flower.name = request.data['name']
        flower.price = request.data['price']
        flower.description = request.data['description']
        flower.image = request.data['image']
        flower.light = request.data['light']
        flower.temp = request.data['temp']
        flower.humidity = request.data['humidity']
        flower.watering = request.data['watering']
        flower.fertilizer = request.data['fertilizer']
        flower.transplantatio = request.data['transplantatio']
        flower.save()
        return Response({"flower": "aaaaaaa"}, status=status.HTTP_200_OK)
    if request.method =='DELETE':
        flower.delete()
        return Response({"serializer.data": "a"}, status=status.HTTP_200_OK)

class ShippingView(APIView):
    def post(self, request):
        flower = Flower.objects.get(id=request.data['flower'])
        Shipping.objects.create(
            name = request.data['name'],
            phone = request.data['phone'],
            flower = flower
        )
        return Response({"fff": 'fff'}, status=status.HTTP_200_OK)
        
    def get(self, request):
        try:
            ships = Shipping.objects.all()
            serializer = ShippingSerializer(ships, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"": ""}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CommentView(APIView):
    def post(self, request):
        flower = Flower.objects.get(id=request.data['id'])
        Comment.objects.create(
            name = request.data['name'],
            text = request.data['text'],
            flower = flower
        )
        return Response({"fff": 'fff'}, status=status.HTTP_200_OK)

    def get(self, request):
        try:
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"": ""}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)