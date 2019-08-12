from django.test import TestCase
from .models import Order, OrderLineItem, Feature
from django.contrib.auth.models import User


class TestOrderModel(TestCase):

    def test_order_add_with_defaults(self):
        order = Order.objects.create(full_name='super', phone_number=3531234567, country='Ireland', postcode="none",
            town_or_city="testtown", street_address1="test1",  street_address2="test2", county="monaghan",date="2020-06-06")
        self.assertEqual(order.full_name, "super")
        self.assertEqual(order.phone_number,3531234567)
        self.assertEqual(order.country, "Ireland")
        self.assertEqual(order.town_or_city, "testtown")
        self.assertEqual(order.street_address1, "test1")
        self.assertEqual(order.street_address2, "test2")
        self.assertEqual(order.county, "monaghan")
        
    def test_orderlineitem_add_with_defaults(self):
        order = Order.objects.create(full_name='super', phone_number=3531234567, country='Ireland', postcode="none",
            town_or_city="testtown", street_address1="test1",  street_address2="test2", county="monaghan",date="2020-06-06")
        author = User.objects.create(username='super', email='author@test.com')
        feature = Feature(name="Create a Test", description="test description", price=30.00, author= author)
        orderlineitem = OrderLineItem(order=order, feature=feature, quantity=2)
        self.assertEqual(orderlineitem.quantity,2)