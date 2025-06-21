from django.test import TestCase
from django.urls import reverse
from users.models import User
from statuses.models import Status
from labels.models import Label
from tasks.models import Task


class TaskCRUDTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='tester', password='12345')
        cls.status = Status.objects.create(name='open')
        cls.label = Label.objects.create(name='urgent')
        cls.task = Task.objects.create(
            name='Test task',
            description='Just a test',
            status=cls.status,
            creator=cls.user,
            executor=cls.user
        )
        cls.task.labels.add(cls.label)

    def test_task_creation(self):
        self.client.login(username='tester', password='12345')
        response = self.client.post(reverse('tasks:create'), {
            'name': 'New task',
            'description': 'A new test task',
            'status': self.status.id,
            'creator': self.user.id,
            'executor': self.user.id,
            'labels': [self.label.id]
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name='New task').exists())

    def test_task_deletion_with_relations(self):
        response = self.client.post(reverse('tasks:delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(id=self.task.id).exists())