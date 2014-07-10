from django.contrib.sites.models import Site

from pinax_theme_bootstrap.conf import settings


def theme(request):
    ctx = {
        "THEME_ADMIN_URL": settings.THEME_ADMIN_URL,
        "THEME_CONTACT_EMAIL": settings.THEME_CONTACT_EMAIL,
    }

    if Site._meta.installed:
        site = Site.objects.get_current()
        ctx.update({
            "SITE_NAME": site.name,
            "SITE_DOMAIN": site.domain
        })

    return ctx
