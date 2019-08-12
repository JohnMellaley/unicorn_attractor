from django.test import TestCase
# from .forms import 
from django.contrib.auth.models import User



def test_viewbug_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")