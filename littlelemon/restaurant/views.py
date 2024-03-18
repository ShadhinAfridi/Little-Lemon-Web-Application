from django.shortcuts import render
from rest_framework import generics,viewsets,permissions
from .serializers import MenuSerializer,BookingSerializer,MenuItemSerializer
from . import models
from django.core import serializers
from datetime import datetime
from .forms import BookingForm
import json, datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset=models.Menu.objects.all()
    serializer_class=MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView,generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated] 
    queryset=models.MenuItem.objects.all()
    serializer_class=MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated] 
    queryset=models.Booking.objects.all()
    def get_queryset(self):
        if self.request.user.username!='admin':
            print(self.request.user.username)
            return models.Booking.objects.filter(Name=self.request.user.username)
        else:
            return models.Booking.objects.all()

    serializer_class = BookingSerializer
    
def about(request):
    return render(request, 'about.html')

# def reservations(request):
#     date = request.GET.get('date',datetime.today().date())
#     bookings = models.Booking.objects.all()
#     booking_json = serializers.serialize('json', bookings)
#     return render(request, 'bookings.html',{"bookings":booking_json})

@csrf_exempt
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
                form.save()
                cleaned_data = form.cleaned_data
                cleaned_data['BookingDate'] = datetime.date.today()
                print(cleaned_data)
                return render(request,'book_successful.html',{'form':cleaned_data})
        else:
            return JsonResponse(form.errors)
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = models.Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = models.Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

