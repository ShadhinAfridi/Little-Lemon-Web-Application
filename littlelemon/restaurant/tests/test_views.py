from django.test import TestCase
from restaurant.views import MenuItemsView
from restaurant.models import Menu
from django.test import Client
from ..serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(MenuID=5,Title="Banana",Price=1,Inventory=1000).save()
        Menu.objects.create(MenuID=4,Title="Drunken Noodles",Price=10,Inventory=1).save()
        
    def test_getall(self):
        response=Client().get(path='/api/menu/')
        self.assertEqual(response.status_code,200)
        serialized_data=MenuSerializer(Menu.objects.all(),many=True).data  
        self.assertEqual(response.data,serialized_data)