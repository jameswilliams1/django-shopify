from django.urls import reverse

from shopify_app.orders.views import OrderCreateView


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
        mocker.patch("shopify_app.orders.views.OrderCreateView.form_class")
        mocker.patch("shopify_app.orders.views.create_order", autospec=True)
        get_response = client.get(reverse("orders:create"))
        assert get_response.status_code == 200

        data = {"some": "data"}
        post_response = client.post(
            reverse("orders:create"),
            data,
            content_type="application/x-www-form-urlencoded",
        )
        # should redirect to all orders on success
        assert post_response.status_code == 302
        assert post_response["Location"] == reverse("orders:all")

    def test_form_valid(self, mocker):
        form = mocker.Mock()
        cleaned_data = {
            "quantity": 1,
            "title": "title",
            "email": "email",
            "price": 100.00,
        }
        form.cleaned_data = cleaned_data
        create_order = mocker.patch(
            "shopify_app.orders.views.create_order", autospec=True
        )

        view = OrderCreateView()
        view.request = mocker.Mock()
        view.form_valid(form)

        expected = {
            "line_items": [{"quantity": 1, "title": "title", "price": 100.00}],
            "email": "email",
        }
        create_order.assert_called_once_with(expected)
