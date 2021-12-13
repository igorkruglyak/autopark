from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Driver, Vehicle


class BlogTests(TestCase):

    @classmethod
    def setUp(cls):
        # Create a driver
        test_driver1 = Driver.objects.create(
            first_name='fname1', last_name='lname1')
        test_driver1.save()

        # Create a vehicle
        test_post = Driver.objects.create(
            first_name='fname1', last_name='lname1')
        test_post.save()
        
        test_vehicle = Vehicle.objects.create(
            driver_id=test_driver1,
            make='make_one',
            vehicle_model='model_one',
            plate_number='AB 7777 AB'
        )
    def test_vehicle(self):
        post = Vehicle.objects.get(id=1)
        driver_id = f'{post.driver_id}'
        make = f'{post.make}'
        vehicle_model = f'{post.vehicle_model}'
        plate_number = f'{post.plate_number}'
        self.assertEqual(driver_id, driver_id)
        self.assertEqual(make, 'make_one')
        self.assertEqual(vehicle_model, 'model_one')
        self.assertEqual(plate_number, 'AB 7777 AB')


