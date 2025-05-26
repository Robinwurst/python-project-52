from django.test import TestCase
from django.urls import reverse
from .models import Status


class StatusTest(TestCase):
    def setUp(self):
        self.status = Status.objects.create(name='Новый статус')

    def test_status_create(self):
        response = self.client.post(reverse('statuses:create'), {'name': 'В работе'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name='В работе').exists())

    def test_status_update(self):
        response = self.client.post(reverse('statuses:update', args=[self.status.id]), {'name': 'Обновлённый статус'})
        self.assertEqual(response.status_code, 302)
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'Обновлённый статус')

    def test_status_delete(self):
        response = self.client.post(reverse('statuses:delete', args=[self.status.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Status.objects.filter(id=self.status.id).exists())