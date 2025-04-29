from django import template

register = template.Library()

@register.filter
def chr_filter(value):
    """Convert integer ASCII value to a character."""
    try:
        return chr(int(value))
    except (ValueError, TypeError):
        return value  
