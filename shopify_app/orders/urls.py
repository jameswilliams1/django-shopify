from django.urls import path

from shopify_app.orders.views import order_create_view, order_list_view

app_name = "orders"

urlpatterns = [
    path("create/", view=order_create_view, name="create"),
    path("all/", view=order_list_view, name="all"),
]
