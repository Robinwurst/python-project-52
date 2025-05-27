from django.test import TestCase
from django.urls import reverse
from users.models import User
from statuses.models import Status
from labels.models import Label
from .models import Task


class TaskTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.status = Status.objects.create(name='Новый')
        self.label = Label.objects.create(name='Баг')
        self.task = Task.objects.create(
            name='Задача',
            description='Описание',
            status=self.status,
            creator=self.user,
            executor=self.user
        )
        self.task.labels.add(self.label)

    def test_task_create(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('tasks:create'), {
            'name': 'Новая задача',
            'description': 'Новое описание',
            'status': self.status.id,
            'executor': self.user.id,
            'labels': [self.label.id]
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name='Новая задача').exists())

    def test_task_delete_only_creator(self):
        other_user = User.objects.create_user(username='other', password='12345')
        self.client.login(username='other', password='12345')

        response = self.client.post(reverse('tasks:delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 403)