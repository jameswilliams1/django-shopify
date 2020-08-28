from django.urls import resolve, reverse


def test_create():
    assert reverse("orders:create") == "/orders/create/"
    assert resolve("/orders/create/").view_name == "orders:create"


def test_all():
    assert reverse("orders:all") == "/orders/all/"
    assert resolve("/orders/all/").view_name == "orders:all"
