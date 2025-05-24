from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Status

User = get_user_model()


class StatusCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.status = Status.objects.create(name='Test Status')

    def test_status_list_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('statuses:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Status')

    def test_status_create_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('statuses:create'), {
            'name': 'New Status'
        }, follow=True)
        self.assertRedirects(response, reverse('statuses:list'))
        self.assertTrue(Status.objects.filter(name='New Status').exists())

    def test_status_update_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('statuses:update', args=[self.status.pk]),
            {'name': 'Updated Status'},
            follow=True
        )
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'Updated Status')
        self.assertRedirects(response, reverse('statuses:list'))

    def test_status_delete_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('statuses:delete', args=[self.status.pk]),
            follow=True
        )
        self.assertRedirects(response, reverse('statuses:list'))
        self.assertFalse(Status.objects.filter(pk=self.status.pk).exists())

    def test_status_delete_protected(self):
        from tasks.models import Task
        self.client.login(username='testuser', password='testpass123')
        task = Task.objects.create(
            name='Test Task',
            status=self.status,
            creator=self.user
        )
        response = self.client.post(
            reverse('statuses:delete', args=[self.status.pk]),
            follow=True
        )
        self.assertTrue(Status.objects.filter(pk=self.status.pk).exists())
        self.assertContains(response, 'Невозможно удалить статус')