import json

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from django.urls import include, path, reverse
from rest_framework.test import APITestCase

from autopark.models import Driver
from autopark.serializers import DriversListSerializer

class DriverApiTestCase(APITestCase):
    """ Test module for create all drivers API """
    def setUp(self):

        self.user = User.objects.create(username="test_user")
        self.driver_one = Driver.objects.create(
            first_name="first_name_one", last_name="'last_name_one"
        )
        self.driver_two = Driver.objects.create(
            first_name="first_name_two", last_name="last_name_two"
        )
        self.driver_three = Driver.objects.create(
            first_name="first_name_three", last_name="last_name_three"
        )
        self.driver_four = Driver.objects.create(
            first_name="first_name_four", last_name="last_name_four"
        )
        

    def test_get_driver(self):
        """ Test module for GET all drivers API """
        response = self.client.get(reverse("driver-list"))
        serializer_data = DriversListSerializer(
            [
                self.driver_one,
                self.driver_two,
                self.driver_three,
                self.driver_four,
                
            ],
            many=True,
        ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_data_filter_gte(self):
        """ Test module for filter_gte data API """
        response = self.client.get(
            reverse("driver-list") + "?created_at__gte=10-11-2021", format="json"
        )
        serializer_data = DriversListSerializer(
            [
                self.driver_one,
                self.driver_two,
                self.driver_three,
                self.driver_four,
                
            ],
            many=True,
        ).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_data_filter_lte(self):
        """ Test module for filter_lte data API """
        response = self.client.get(
            reverse("driver-list") + "?created_at__lte=16-11-2021", format="json"
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual([], response.data)

    def test_create_driver(self):
        """ Test module for create single driver API """
        self.assertEqual(4, Driver.objects.all().count())
        data = {"first_name": "First_Name", "last_name": "Last_Name"}
        response = self.client.post(
            reverse("driver-list"), data=data, format="json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Driver.objects.all().count())

    def test_update_driver(self):
        """ Test module for update single driver API """
        data = {"first_name": "First_Name", "last_name": "Last_Name"}
        self.client.force_login(self.user)
        response = self.client.put(
            reverse("driver-detail", kwargs={"pk": self.driver_three.id}),
            data=data,
            format="json",
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.driver_three.refresh_from_db()
        self.assertEqual(data["first_name"], self.driver_three.first_name)

    def test_delete_driver(self):
        """ Test module for delete single driver API """
        self.client.force_login(self.user)
        response = self.client.delete(
            reverse("driver-detail", kwargs={"pk": 4}))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(4, Driver.objects.all().count())

    def test_not_driver(self):
        """ Test module for not exist driver API """
        response = self.client.get(reverse("driver-detail", kwargs={"pk": 25}))
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
