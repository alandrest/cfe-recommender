from django.template.defaulttags import register
from src.rating.models import Rating

@register.filter
def get_dict_val(dictionary, key, key_as_str=True):
    if not isinstance(dictionary, dict):
        return None
    rc = dictionary.get(key)
    if rc is None and key_as_str:
        key = f"{key}"
        rc = dictionary.get(key)
    return rc

@register.filter
def get_object_rating(user, object_id):
    Rating.objects.get(user=user, object_id=object_id)