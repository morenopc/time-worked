from django import template

register = template.Library()


@register.simple_tag
def get(qs, **kwargs):
    """Template tag which allows queryset get.
    Usage:
      {% get QuerySet field=value as object %}
      {{ object.name }}
    """
    try:
        return qs.get(**kwargs)
    except Exception:
        return None


@register.simple_tag
def filter(qs, **kwargs):
    """Template tag which allows queryset filter.
    Usage:
      {% filter QuerySet field=value as filtered_queryset %}
      {% for object in filtered_queryset %}
        {{ object.name }}
      {% endfor %}
    """
    try:
        return qs.filter(**kwargs)
    except Exception:
        return None
