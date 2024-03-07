import json
import base64
import datetime
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from trips.models import User, Driver, Trip
from trips.serializers import UserSerializer, LoginSerializer, TripSerializer, DriverSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from trips.utils import VEHICLE_TYPES


class UserSignUpViewTest(TestCase):
    def test_user_signup_view(self):
        client = Client()
        data = {
            'full_name': 'Test User',
            'phone_number': '1234567890',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = client.post(reverse('api/user/sign_up'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email=data['email']).exists())

class UserLoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(full_name='Test User', email='test@example.com', password='testpassword', phone_number='0834568900')

    def test_login_view(self):
        client = Client()
        data = {'email': 'test@example.com', 'password': 'testpassword'}
        response = client.post(reverse('api/user/login'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

class DriverSignUpViewTest(TestCase):
    def test_driver_signup_view(self):
        client = Client()
        data = {
            'full_name': 'Test Driver',
            'phone_number': '1234567890',
            'email': 'driver@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'physical_address': '123 Main St',
            'vehicle_registration': 'ABC123',
            'vehicle_type': VEHICLE_TYPES[0][0],
            'licence_no': '123456',
        }
        response = client.post(reverse('api/driver/sign_up'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Driver.objects.filter(email=data['email']).exists())

class DriverLoginViewTest(TestCase):
    def setUp(self):
        self.driver = Driver.objects.create_driver(
            full_name='Test Driver',
            phone_number='1234567890',
            email='driver@example.com',
            password='testpassword',
            physical_address='123 Main St',
            vehicle_registration='ABC123',
            vehicle_type=VEHICLE_TYPES[0][0],
            licence_no='123456',
            )
    def test_login_view(self):
        client = Client()
        data = {'email': 'driver@example.com', 'password': 'testpassword'}
        response = client.post(reverse('api/user/login'), data=data)
        access = response.data['access']
        header, payload, signature = access.split('.')
        decoded_payload = base64.b64decode(f'{payload}==')
        payload_data = json.loads(decoded_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        




class TripViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(full_name='Test User', email='test@example.com', password='testpassword', phone_number='0834568900')


    def test_trip_view(self):
        client = Client()
        data = {'email': 'test@example.com', 'password': 'testpassword'}
        response = client.post(reverse('api/user/login'), data=data)
        self.access = response.data['access']
        trip = Trip.objects.create(
                pickup_location='23 Main avenue',
                dropoff_location='100 Kent Avenue',
                vehicle_type=VEHICLE_TYPES[0][0],
                number_of_floors=2,
                load_description='This is a test load description.',
                pickup_time=f'{datetime.date.today()}',
                bid=500,
                )
        res = self.client.get('/api/trip', HTTP_AUTHORIZATION=f'Bearer {self.access}')
        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertTrue(Trip.objects.filter(id=res.data[0]['id']).exists())
        self.assertEqual(res.data[0]['id'], str(trip.id))
        self.assertEqual(res.data[0]['pickup_location'], trip.pickup_location)
        self.assertEqual(res.data[0]['dropoff_location'], trip.dropoff_location)
        self.assertEqual(res.data[0]['load_description'], trip.load_description)
        


    
