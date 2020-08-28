import requests
from django.conf import settings

from shopify_app.orders.exceptions import ShopifyResponseException


def get_all_orders():
    """Get a list of dicts of all orders from Shopify.

    Returns:
        list: each order in the inventory as a dict
    """
    response = requests.get(
        settings.SHOPIFY_ORDERS_URL,
        auth=(settings.SHOPIFY_API_KEY, settings.SHOPIFY_PASSWORD),
    )
    return response.json()["orders"]


def create_order(order):
    """Create a new order in Shopify.

    Params:
        order: the order to create as a dict
    """
    response = requests.post(
        settings.SHOPIFY_ORDERS_URL,
        auth=(settings.SHOPIFY_API_KEY, settings.SHOPIFY_PASSWORD),
        json={"order": order},
    )
    if response.status_code != 201:
        raise ShopifyResponseException(
            f"The Shopify API returned an invalid response:\n{response.text}"
        )
