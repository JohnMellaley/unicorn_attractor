from django.test import TestCase
from .models import Bug

# Create your tests here.
class BugTests(TestCase):
    
    def test_str(self):
        test_name = Bug(name = 'A bug')
        self.assertEqual(str(test_name), 'A bug')