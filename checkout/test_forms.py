from django.test import TestCase
from .forms import MakePaymentForm, OrderForm

# Create your tests here.
class TestOrderForm(TestCase):

    def test_can_add_OrderForm(self):
        form = OrderForm({'full_name':'test', 'phone_number': '+35311276632', 'country':'ireland','postcode':'bvf56'
            ,'town_or_city':'navan', 'street_address1':'street1','street_address2':'street2','county':'meath'})
        self.assertTrue(form.is_valid())
    
    def test_postcode_is_blank(self):
        form = OrderForm({'full_name':'test', 'phone_number': '+012232882433', 'country':'ireland','postcode':''
        ,'town_or_city':'navan', 'street_address1':'street1','street_address2':'street2','county':'meath'})
        self.assertTrue(form.is_valid())
        
    def test_country_is_blank(self):
        form = OrderForm({'full_name':'test', 'phone_number': '+012232882433', 'country':'','postcode':''
        ,'town_or_city':'navan', 'street_address1':'street1','street_address2':'street2','county':'meath'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors,{'country': ['This field is required.']} )
        
    def test_phone_is_incorrect(self):
       form = OrderForm({'full_name':'test', 'phone_number': '1234567', 'country':'ireland','postcode':''
        ,'town_or_city':'navan', 'street_address1':'street1','street_address2':'street2','county':'meath'})
       self.assertFalse(form.is_valid())
       self.assertEqual(form.errors,{'phone_number': ['invalid phone number']})
        
class TestMakePaymentForm(TestCase):
    
    def test_add_MakePaymentForm(self):
        form = MakePaymentForm({'credit_card_number':'323232323','cvv':'123','expiry_month':'11','expiry_year':'2020','stripe_id':'42424242'})
        self.assertTrue(form.is_valid())
    
    def test_blank_invalid_month(self):
        form = MakePaymentForm({'credit_card_number':'323232323','cvv':'123','expiry_month':'13','expiry_year':'2020','stripe_id':'42424242'})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
    
    def test_blank_invalid_year(self):
        form = MakePaymentForm({'credit_card_number':'323232323','cvv':'123','expiry_month':'12','expiry_year':'2016','stripe_id':'42424242'})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)