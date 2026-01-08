from django import template
register = template.Library()

@register.filter
def get_ghost(post):
    """Safely retrieves the ghost_post related object."""
    try:
        return post.ghost_post
    except Exception:
        return None
