from django.shortcuts import render
from api.models import Flower
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from api.serializers import FlowerSerilizer
from rest_framework.views import status
@api_view(['GET'])
def flower_list(request):
    try:
        flowers = Flower.objects.all()
        serializer = FlowerSerilizer(flowers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def flower_detailed(request, flower_id):
    try:
        flower = Flower.objects.get(id=id)
        serializer = FlowerSerilizer(flower)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

