from django.test import TestCase
from .models import MenuItem, Booking
from rest_framework.test import APIClient
from rest_framework import status
from  .serializers import BookingSerializer, MenuItemSerializer

import json

class MenuItemsViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Create some test menu items
        MenuItem.objects.create(title='Item 1', price=10.99, inventory=20)
        MenuItem.objects.create(title='Item 2', price=15.99, inventory=15)

        # Initialize the API client and authenticate the user
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_menu_items(self):
        # Send GET request to the endpoint
        response = self.client.get('/api/menu-items/')

        # Retrieve all menu items from the database
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data matches the serialized menu items
        self.assertEqual(response.data, serializer.data)

    def test_create_menu_item(self):
        # Data for creating a new menu item
        new_menu_item_data = {'title': 'New Item', 'price': 12.99, 'inventory': 10}

        # Send POST request to create a new menu item
        response = self.client.post('/api/menu-items/', new_menu_item_data, format='json')

        # Check if the response status code is 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the menu item was created successfully in the database
        self.assertTrue(MenuItem.objects.filter(title='New Item').exists())

        # Retrieve the created menu item from the database
        created_menu_item = MenuItem.objects.get(title='New Item')

        # Check if the created menu item attributes match the provided data
        self.assertEqual(created_menu_item.title, new_menu_item_data['title'])
        self.assertEqual(created_menu_item.price, new_menu_item_data['price'])
        self.assertEqual(created_menu_item.inventory, new_menu_item_data['inventory'])


class BookingViewSetTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Create some test bookings
        Booking.objects.create(name='Test Booking 1', no_of_guests=5, bookingdate='2024-02-25T12:00:00Z')
        Booking.objects.create(name='Test Booking 2', no_of_guests=3, bookingdate='2024-02-26T12:00:00Z')

        # Initialize the API client and authenticate the user
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_bookings(self):
        # Send GET request to the endpoint
        response = self.client.get('/api/bookings/')

        # Retrieve all bookings from the database
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data matches the serialized bookings
        self.assertEqual(response.data, serializer.data)

    def test_create_booking(self):
        # Data for creating a new booking
        new_booking_data = {'name': 'New Booking', 'no_of_guests': 4, 'bookingdate': '2024-02-27T12:00:00Z'}

        # Send POST request to create a new booking
        response = self.client.post('/api/bookings/', new_booking_data, format='json')

        # Check if the response status code is 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the booking was created successfully in the database
        self.assertTrue(Booking.objects.filter(name='New Booking').exists())

        # Retrieve the created booking from the database
        created_booking = Booking.objects.get(name='New Booking')

        # Check if the created booking attributes match the provided data
        self.assertEqual(created_booking.name, new_booking_data['name'])
        self.assertEqual(created_booking.no_of_guests, new_booking_data['no_of_guests'])
        self.assertEqual(str(created_booking.bookingdate), new_booking_data['bookingdate'])   