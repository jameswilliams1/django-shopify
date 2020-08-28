from django.forms import CharField, EmailField, Form, IntegerField


class OrderCreateForm(Form):
    email = EmailField(required=False)
    title = CharField()
    quantity = IntegerField()
