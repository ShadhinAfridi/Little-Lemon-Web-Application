from django.test import TestCase
from restaurant.models import MenuItem,Booking

class MenuTest(TestCase):
    def test_menu(self):
        item=MenuItem.objects.create(title="Ice Cream",price=5,inventory=100)
        self.assertEqual(str(item),"Ice Cream: 5")