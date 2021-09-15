from bedavailability.models import Availability
from django import template

register = template.Library()


@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success'
    return 'bg-danger'


@register.simple_tag
def get_availibilities(hospital):
    return Availability.objects.filter(hospital=hospital).order_by('facility_id')


@register.simple_tag
def is_option_selected(selected_option, pk):
    if selected_option == str(pk):
        return 'selected'
    return ''