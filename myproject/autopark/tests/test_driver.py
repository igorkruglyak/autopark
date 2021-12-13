from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Driver


class DriverTests(TestCase):

    @classmethod
    def setUp(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

        # Create a blog driver
        test_post = Driver.objects.create(
            first_name='fname1', last_name='lname1')
        test_post.save()

    def test_driver(self):
        post = Driver.objects.get(id=1)
        first_name = f'{post.first_name}'
        last_name = f'{post.last_name}'
        self.assertEqual(first_name, 'fname1')
        self.assertEqual(last_name, 'lname1')
        