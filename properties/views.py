from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Property
from django.http import JsonResponse
from .utils import get_all_properties, get_redis_cache_metrics

# Create your views here.

@cache_page(60 * 15)
def property_list(request):

    properties = Property.objects.all().values(
        'id', 'title', 'description', 'price', 'location', 'created_at'
    )
    return JsonResponse({"data": list(properties)})

def redis_metrics(request):
    return JsonResponse(get_redis_cache_metrics)