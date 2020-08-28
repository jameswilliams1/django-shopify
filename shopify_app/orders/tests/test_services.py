from base64 import urlsafe_b64encode

from django.conf import settings
from requests_mock import ANY as ANY_URL

from shopify_app.orders.services import get_all_orders


def test_get_all_orders(requests_mock):
    orders = [{"id": 1, "number": 65, "name": "#1065"}]
    requests_mock.get(ANY_URL, json={"orders": orders})

    result = get_all_orders()

    assert result == orders

    request = requests_mock.last_request
    auth_key = urlsafe_b64encode(
        f"{settings.SHOPIFY_API_KEY}:{settings.SHOPIFY_PASSWORD}".encode("utf-8")
    )

    assert request.headers.get("Authorization") == f"Basic {auth_key.decode('utf-8')}"
    assert request.url == settings.SHOPIFY_ORDERS_URL
