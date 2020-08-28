from django.forms import CharField, EmailField, FloatField, Form, IntegerField


class OrderCreateForm(Form):
    email = EmailField(required=False)
    title = CharField()
    quantity = IntegerField()
    price = FloatField()
