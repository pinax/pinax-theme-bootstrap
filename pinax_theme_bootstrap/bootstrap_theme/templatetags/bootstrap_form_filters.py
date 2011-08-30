from django.template import Context
from django.template.loader import get_template
from django import template


register = template.Library()


@register.filter
def as_bootstrap(form):
    template = get_template("bootstrap/form.html")
    c = Context({"form": form})
    return template.render(c)
