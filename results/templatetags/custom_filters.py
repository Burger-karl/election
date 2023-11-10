# your_app/templatetags/custom_filters.py
from django import template
from results.models import Party

register = template.Library()

@register.filter(name='get_by_id')
def get_by_id(party_id, party_list):
    try:
        party_id = int(party_id)
        return next(obj for obj in party_list if getattr(obj, 'id', None) == party_id)
    except (StopIteration, ValueError):
        return None
