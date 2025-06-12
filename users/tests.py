from django.test import TestCase
from django.urls import reverse
from .models import User


class UserCRUDTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='user1', password='12345', first_name='John', last_name='Doe')
        cls.other_user = User.objects.create_user(username='other', password='12345')

    def test_user_creation(self):
        response = self.client.post(reverse('users:create'), {
            'username': 'new_user',
            'password1': 'securepass123',
            'password2': 'securepass123',
            'first_name': 'Jane',
            'last_name': 'Smith'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='new_user').exists())

    def test_user_deletion(self):
        response = self.client.post(reverse('users:delete', args=[self.user.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(id=self.user.id).exists())