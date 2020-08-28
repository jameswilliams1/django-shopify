from django.views.generic import CreateView, TemplateView

from shopify_app.orders.services import get_all_orders


class OrderCreateView(CreateView):
    ...


order_create_view = OrderCreateView.as_view()


class OrderListView(TemplateView):
    template_name = "orders/order_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = get_all_orders()
        return context


order_list_view = OrderListView.as_view()
