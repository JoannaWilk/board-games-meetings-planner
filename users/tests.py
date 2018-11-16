from django.test import TestCase
from django.urls import reverse

from .models import CustomUser


class UserModelTests(TestCase):

    def create_user(self, username, email, password):
        """Create user with given username, email and passwords"""
        return CustomUser.objects.create(
            username=username,
            email=email,
            password=password
        )

    def test_user_creation(self):
        user = self.create_user(
            username='testuser', email='test@user.com', password='123ABC'
        )
        self.assertTrue(isinstance(user, CustomUser))
        self.assertEqual(user.__str__(), user.username)
