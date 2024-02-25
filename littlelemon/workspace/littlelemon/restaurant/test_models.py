from django.test import TestCase
from .models import MenuItem, Booking


class MenuItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        MenuItem.objects.create(title='Test Item', price=10.99, inventory=20)
    
    def test_title_max_length(self):
        item = MenuItem.objects.get(id=1)
        max_length = item._meta.get_field('title').max_length
        self.assertEquals(max_length, 255)

    def test_price_decimal_places(self):
        item = MenuItem.objects.get(id=1)
        decimal_places = item._meta.get_field('price').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_price_max_digits(self):
        item = MenuItem.objects.get(id=1)
        max_digits = item._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 10)

    def test_inventory_integer_field(self):
        item = MenuItem.objects.get(id=1)
        inventory = item._meta.get_field('inventory').get_internal_type()
        self.assertEquals(inventory, 'IntegerField')

    def test_object_str_representation(self):
        item = MenuItem.objects.get(id=1)
        expected_object_name = f'{item.title} : {str(item.price)}'
        self.assertEquals(expected_object_name, str(item))
        
class BookingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Booking.objects.create(name='Test Booking', no_of_guests=5, bookingdate='2024-02-25 12:00:00')
    
    def test_name_max_length(self):
        booking = Booking.objects.get(id=1)
        max_length = booking._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_no_of_guests_integer_field(self):
        booking = Booking.objects.get(id=1)
        no_of_guests = booking._meta.get_field('no_of_guests').get_internal_type()
        self.assertEquals(no_of_guests, 'IntegerField')

    def test_bookingdate_type(self):
        booking = Booking.objects.get(id=1)
        bookingdate_type = booking._meta.get_field('bookingdate').get_internal_type()
        self.assertEquals(bookingdate_type, 'DateTimeField')