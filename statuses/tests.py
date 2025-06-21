from django.test import TestCase
from django.urls import reverse

from users.models import User
from statuses.models import Status


class StatusCRUDTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.status = Status.objects.create(name='to_delete')

    def setUp(self):
        self.client.force_login(self.user)

    def test_status_creation(self):
        response = self.client.post(reverse('statuses:create'), {
            'name': 'in_progress'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name='in_progress').exists())

    def test_status_update(self):
        response = self.client.post(reverse('statuses:update', args=[self.status.id]), {
            'name': 'updated_status'
        })
        self.assertEqual(response.status_code, 302)
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'updated_status')

    def test_status_delete(self):
        response = self.client.post(reverse('statuses:delete', args=[self.status.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Status.objects.filter(id=self.status.id).exists())