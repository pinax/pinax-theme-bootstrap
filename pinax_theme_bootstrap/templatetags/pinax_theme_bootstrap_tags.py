from django import template

register = template.Library()


@register.simple_tag()
def get_message_tags(message):
    """
    Returns tags for a message
    """
    if message.tags:
        return u"alert-{tags}".format(tags=message.tags)
    return u""
