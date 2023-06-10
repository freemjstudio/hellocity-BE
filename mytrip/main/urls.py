from django.urls import path

from . import views

urlpatterns = [
    path('', views.index), # config/urls.py 에서 main/ 에 매핑됨
    path('hotel', views.hotelListAPI),
    path('list', views.dataListAPI),
]