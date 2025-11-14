from django.core.cache import cache
from .models import Property
import logging
from django_redis import get_redis_connection

def get_all_properties():
    all_properties = cache.get('all_properties')
    if all_properties is None:
        all_properties = list(Property.objects.all().values(
            'id', 'title', 'desctiption', 'price', 'location', 'created_at'
        ))

        cache.set('all_properties', all_properties, 3600)
    return all_properties

logger = logging.getLogger(__name__)

def get_redis_cache_redis():
    try:
        redis_conn = get_redis_connection('default')
        info = redis_conn.info()

        hits = info.get('keyspace_hits', 0)
        misses = info.get('keyspace_misses', 0)

        total = hits + misses
        hit_ratio = (hits / total) if total > 0 else 0

        metric = {
            'hits': hits,
            'misses': misses,
            'hit_ratio': round(hit_ratio, 4)
        }

        logger.info(f"Redis Cache Metrics: {metric}")

        return metric
    
    except Exception as e:
        logger.error(f"Error retrieving metrics: {e}")
        return {
            'hits': 0,
            'misses': 0,
            'hit_ratio': 0
        }