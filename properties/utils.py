from django.core.cache import cache
from .models import Property

def get_all_properties():
    all_properties = cache.get('all_properties')
    if all_properties is None:
        all_properties = list(Property.objects.all().values(
            'id', 'title', 'desctiption', 'price', 'location', 'created_at'
        ))

        cache.set('all_properties', all_properties, 3600)
    return all_properties