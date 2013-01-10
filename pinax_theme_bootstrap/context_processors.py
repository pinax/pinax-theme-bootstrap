from pinax_theme_bootstrap.conf import settings


def theme(request):
    ctx = {
        "THEME_ADMIN_URL": settings.THEME_ADMIN_URL,
        "THEME_CONTACT_EMAIL": settings.THEME_CONTACT_EMAIL,
    }
    return ctx
