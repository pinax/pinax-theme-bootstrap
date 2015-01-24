from django import template
from django.contrib.messages.utils import get_level_tags
from django.utils.encoding import force_text


LEVEL_TAGS = get_level_tags()

register = template.Library()


@register.simple_tag()
def get_message_tags(message):
    """
    Returns the message's level_tag prefixed with Bootstrap's "alert-" prefix
    along with any tags included in message.extra_tags

    Messages in Django >= 1.7 have a message.level_tag attr
    """
    level_tag = force_text(LEVEL_TAGS.get(message.level, ''), strings_only=True)
    if level_tag == u"error":
        # Alias the error tag as danger, since .alert-error no longer exists
        # in Bootstrap 3
        level_tag = u"danger"

    if level_tag:
        alert_level_tag = u"alert-{tag}".format(tag=level_tag)
    else:
        alert_level_tag = None

    extra_tags = force_text(message.extra_tags, strings_only=True)

    if extra_tags and alert_level_tag:
        return u' '.join([extra_tags, alert_level_tag])
    elif extra_tags:
        return extra_tags
    elif alert_level_tag:
        return alert_level_tag
    return u''
