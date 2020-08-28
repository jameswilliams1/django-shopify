from django.views.generic import View


class OrderCreateView(View):
    ...


order_create_view = OrderCreateView.as_view()


class OrderListView(View):
    ...


order_list_view = OrderListView.as_view()
