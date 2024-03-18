from django.db import models
import datetime

# Create your models here.
class Booking(models.Model):
    TableID=models.IntegerField()
    Name=models.CharField(max_length=255, blank=False)
    No_of_guests=models.IntegerField(blank=False)
    BookingDate=models.DateField(default=datetime.date.today)
    def __str__(self):
        return f'{self.Name}: {str(self.TableID)}: {str(self.BookingDate)}'

class Menu(models.Model):
    MenuID=models.IntegerField()
    Title=models.CharField(max_length=255)
    Price=models.DecimalField(max_digits=6,decimal_places=2)
    Inventory=models.IntegerField()
    def __str__(self):
        return f'{self.Title}: {str(self.Price)}'

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()    
    def __str__(self):
        return f'{self.title}: {str(self.price)}'
    