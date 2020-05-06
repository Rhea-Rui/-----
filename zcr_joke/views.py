from django.shortcuts import render
from .models import *
from .serializers import CrossSerializer,HotCrossSerializer,PicturesCrossSerializer,GoodsSerializer,TreadSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .permissions import IsOwnerOrReadOnly
from django.http import JsonResponse
from rest_framework import status
# Create your views here.



from .custom_model_view_set import CustomModelViewSet

class CrossSet(CustomModelViewSet):

    queryset = Cross.objects.all()
    serializer_class = CrossSerializer


class HotCrossSet(CustomModelViewSet):

    queryset = HotCross.objects.all()
    serializer_class = HotCrossSerializer


class PicturesCrossSet(CustomModelViewSet):

    queryset = PicturesCross.objects.all()
    serializer_class = PicturesCrossSerializer


class GoodsSet(CustomModelViewSet):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    authentication_classes = [JSONWebTokenAuthentication]

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class TreadSet(CustomModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = [JSONWebTokenAuthentication]

    queryset = Tread.objects.all()
    serializer_class = TreadSerializer

