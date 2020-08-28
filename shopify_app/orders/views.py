from django.contrib.messages.views import SuccessMessageMixin
from django.urls.base import reverse_lazy
from django.views.generic import FormView, TemplateView

from shopify_app.orders.forms import OrderCreateForm
from shopify_app.orders.services import get_all_orders


class OrderCreateView(SuccessMessageMixin, FormView):
    template_name = "orders/order_create_form.html"
    form_class = OrderCreateForm
    success_url = reverse_lazy("orders:all")
    success_message = "Order added successfully."


order_create_view = OrderCreateView.as_view()


class OrderListView(TemplateView):
    template_name = "orders/order_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = get_all_orders()
        return context


order_list_view = OrderListView.as_view()
