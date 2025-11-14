from django.urls import path
from .views import property_list, redis_metrics

urlpatterns = [
    path('properties/', property_list, name='property_list'),
    path('metrics/redis/', redis_metrics),
]