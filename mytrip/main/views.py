from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(" hello city team ")

def hotel(request):
    return HttpResponse("hotel data")