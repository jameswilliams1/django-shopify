# SHOPIFY_GET_ORDERS_URL
# SHOPIFY_CREATE_ORDER_URL
# SHOPIFY_ACCESS_TOKEN
# SHOPIFY_API_KEY
# SHOPIFY_PASSWORD
# SHOPIFY_SHARED_SECRET
import requests
from django.conf import settings


def get_all_orders():
    """Get a list of dicts of all orders from Shopify.

    Returns:
        list: each order in the inventory as a dict
    """
    response = requests.get(
        settings.SHOPIFY_GET_ORDERS_URL,
        auth=(settings.SHOPIFY_API_KEY, settings.SHOPIFY_PASSWORD),
    )
    return response.json()["orders"]


def create_order(order):
    """Create a new order in Shopify.

    Params:
        order: the order to create as a dict

    Returns:
        # TODO
    """
