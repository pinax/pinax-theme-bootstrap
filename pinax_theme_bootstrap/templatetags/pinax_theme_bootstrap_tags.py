from django import template
from django.contrib.messages.utils import get_level_tags


LEVEL_TAGS = get_level_tags()

register = template.Library()


@register.simple_tag()
def get_message_tags(message):
    """
    Returns the message's level_tag prefixed with Bootstrap's "alert-" prefix
    along with any tags included in message.extra_tags

    Messages in Django >= 1.7 have a message.level_tag attr
    """
    level_tag = LEVEL_TAGS[message.level]
    if level_tag == u"error":
        level_tag = u"danger"

    alert_level_tag = u"alert-{tag}".format(tag=level_tag)

    tags = [alert_level_tag]
    if message.extra_tags:
        tags.append(message.extra_tags)

    return u" ".join(tags)
