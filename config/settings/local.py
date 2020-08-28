from .base import *  # noqa
from .base import env

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="jy-1sdubky(jmkm%=(gy*62lm*ij*alin3(9ozuz7i7sxqs*(i",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# django-debug-toolbar
INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
INTERNAL_IPS = ["127.0.0.1"]
