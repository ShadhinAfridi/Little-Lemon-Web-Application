from rest_framework import serializers 
from .models import Menu,Booking,MenuItem

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields="__all__"
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields="__all__"
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        fields="__all__"