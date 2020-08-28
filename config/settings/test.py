from .base import *  # noqa
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="jy-1sdubky(jmkm%=(gy*62lm*ij*alin3(9ozuz7i7sxqs*(i",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# Shopify
SHOPIFY_GET_ORDERS_URL = "https://example.com/view"
SHOPIFY_CREATE_ORDER_URL = "https://example.com/create"
SHOPIFY_ACCESS_TOKEN = "token"
SHOPIFY_API_KEY = "key"
SHOPIFY_PASSWORD = "password"
SHOPIFY_SHARED_SECRET = "secret"
