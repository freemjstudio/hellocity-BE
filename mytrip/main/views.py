from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import barrier_free_hotel, categorized
from rest_framework.views import APIView
from .serializers import HotelSerializer, CategorySerializer

def index(request):
    return HttpResponse(" hello city team ")

def hotelListAPI(request):
    # def get(self, request):
    #     queryset = barrier_free_hotel.objects.all()
    #     print(queryset)
    #     serializer = HotelSerializer(queryset, many=True)
    #     return Response(serializer.data)
    hotel_list = barrier_free_hotel.objects.all()
    context = {'hotel_list':hotel_list}
    print(context)
    return render(request, 'main/hotel_list.html', context)

def dataListAPI(request):
    data_list = categorized.objects.all()
    context = {'data_list':data_list}
    print(context)
    return render(request, 'main/data_list.html', context)

def get_activity(request):
    return

def get_healing(request):
    return

def get_restaurant(request):
    return

def get_explore(request):
    return