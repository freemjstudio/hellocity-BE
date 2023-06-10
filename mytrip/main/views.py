from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import barrier_free_hotel, categorized, transportation
from rest_framework.views import APIView
from .serializers import HotelSerializer, CategorySerializer
from rest_framework import viewsets

from django.core import serializers

def index(request):
    return HttpResponse(" hello city team backend")


def hotelListAPI(request):
    hotel_list = barrier_free_hotel.objects.all().values()
    context = {'hotel_list':hotel_list}
    # print(context)
    return render(request, 'main/hotel_list.html', context)

def dataListAPI(request):
    data_list = categorized.objects.all().values()
    context = {'data_list':data_list}
    # print(context)
    return render(request, 'main/data_list.html', context)

def activityAPI(request):
    activity_list = categorized.objects.filter(category='액티비티').values()
    context = {'activity_list': activity_list, }
    # print(context)
    return render(request, 'main/activity_list.html', context)

def healingAPI(request):
    healing_list = categorized.objects.filter(category='힐링').values()
    context = {'healing_list': healing_list}
    # print(context)
    return render(request, 'main/healing_list.html', context)

def restaurantAPI(request):
    restaurant_list = categorized.objects.filter(category='맛집').values()
    context = {'restaurant_list':restaurant_list}
    # print(context)
    return render(request, 'main/restaurant_list.html', context)

def exploreAPI(request):
    explore_list = categorized.objects.filter(category='탐구').values()
    context = {'explore_list':explore_list}
    # print(context)
    return render(request, 'main/explore_list.html', context)
