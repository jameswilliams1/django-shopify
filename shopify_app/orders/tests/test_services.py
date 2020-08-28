from base64 import urlsafe_b64encode

import pytest
from django.conf import settings

from shopify_app.orders.exceptions import ShopifyResponseException
from shopify_app.orders.services import create_order, get_all_orders


def test_get_all_orders(requests_mock):
    orders = [{"id": 1, "number": 65, "name": "#1065"}]
    requests_mock.get(settings.SHOPIFY_ORDERS_URL, json={"orders": orders})

    result = get_all_orders()

    assert result == orders

    request = requests_mock.last_request
    auth_key = urlsafe_b64encode(
        f"{settings.SHOPIFY_API_KEY}:{settings.SHOPIFY_PASSWORD}".encode("utf-8")
    )

    assert request.headers.get("Authorization") == f"Basic {auth_key.decode('utf-8')}"


def test_create_order_success(requests_mock):
    requests_mock.post(settings.SHOPIFY_ORDERS_URL, status_code=201)
    order = {"some": "order"}

    create_order(order)

    request = requests_mock.last_request
    auth_key = urlsafe_b64encode(
        f"{settings.SHOPIFY_API_KEY}:{settings.SHOPIFY_PASSWORD}".encode("utf-8")
    )
    assert request.json() == {"order": order}
    assert request.headers.get("Authorization") == f"Basic {auth_key.decode('utf-8')}"


def test_create_order_bad_response(requests_mock):
    requests_mock.post(settings.SHOPIFY_ORDERS_URL, status_code=400)

    with pytest.raises(ShopifyResponseException):
        create_order({})
