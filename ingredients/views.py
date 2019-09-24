from django.shortcuts import render
from .models import Dish
from .serializers import DishSerializer
from rest_framework import generics

# Create your views here.
class DishListCreate(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer