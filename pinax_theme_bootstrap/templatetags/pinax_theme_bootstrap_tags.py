from django import template
from django.contrib.messages.utils import get_level_tags


LEVEL_TAGS = get_level_tags()

register = template.Library()


@register.simple_tag()
def get_message_tags(message):
    """
    Returns tags for a message
    """
    level_name = LEVEL_TAGS[message.level]
    level_tag = u"alert-{name}".format(name=level_name)

    tags = [level_tag]
    if message.extra_tags:
        tags.append(message.extra_tags)

    return u" ".join(tags)
