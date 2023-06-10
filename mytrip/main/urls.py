from django.urls import path
from rest_framework import routers
from . import views


# router = routers.DefaultRouter()
# router.register('Hotel', views.barrier_free_hotel)
# router.register('Category', views.categorized)

urlpatterns = [
    path('', views.index), # config/urls.py 에서 main/ 에 매핑됨
    path('hotel', views.hotelListAPI),
    path('list', views.dataListAPI),
    path('activity', views.activityAPI),
    path('healing', views.healingAPI),
    path('restaurant', views.restaurantAPI),
    path('explore', views.exploreAPI),
]