from django.views.generic import CreateView, ListView


class OrderCreateView(CreateView):
    ...


order_create_view = OrderCreateView.as_view()


class OrderListView(ListView):
    ...


order_list_view = OrderListView.as_view()
