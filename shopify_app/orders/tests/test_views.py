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


class TestOrderCreateView:
    def test_create_loads_form(self, mocker, client):
        mocker.patch("shopify_app.orders.views.OrderCreateForm", autospec=True)

        get_response = client.get(reverse("orders:create"))
        assert get_response.status_code == 200

        data = {"some": "data"}
        post_response = client.post(
            reverse("orders:create"),
            data,
            content_type="application/x-www-form-urlencoded",
        )
        # should redirect or all orders
        assert post_response.status_code == 302
        assert post_response["Location"] == reverse("orders:all")
