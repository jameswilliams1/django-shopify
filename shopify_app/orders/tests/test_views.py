from django.urls import reverse


class TestOrderListView:
    def test_get_populates_context(self, mocker, client):
        get_orders = mocker.patch(
            "shopify_app.orders.views.get_all_orders", autospec=True
        )
        response = client.get(reverse("orders:all"))

        assert response.status_code == 200
        get_orders.assert_called_once_with()
        assert response.context.get("orders") == get_orders.return_value
