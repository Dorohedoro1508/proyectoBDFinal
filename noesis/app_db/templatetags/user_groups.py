from django import template

register = template.Library()

@register.filter
def has_group(user, group_name):
    """Evalúa si el usuario pertenece al grupo especificado."""
    return user.groups.filter(name=group_name).exists()
