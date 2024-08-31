from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="testpassword")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")