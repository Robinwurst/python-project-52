from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from tasks.models import Task
from statuses.models import Status


User = get_user_model()


class UserCRUDTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.status = Status.objects.create(name='new_status')

        cls.user = User.objects.create_user(
            username='user1',
            password='12345',
            first_name='John',
            last_name='Doe'
        )
        cls.other_user = User.objects.create_user(
            username='other',
            password='12345'
        )


        cls.task = Task.objects.create(
            name='Test task',
            description='Description',
            status=cls.status,
            creator=cls.user,
            executor=cls.other_user
        )

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

    def test_user_cannot_be_deleted_if_used_as_creator(self):

        self.client.force_login(self.user)

        response = self.client.post(reverse('users:delete', args=[self.user.id]))


        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:index'))


        self.assertTrue(User.objects.filter(id=self.user.id).exists())


        messages_list = list(response.wsgi_request._messages)
        self.assertTrue(any("используется" in str(msg) for msg in messages_list))

    def test_user_can_be_deleted_if_not_used(self):

        new_user = User.objects.create_user(
            username='new_user',
            password='testpass123'
        )
        self.client.force_login(new_user)

        response = self.client.post(reverse('users:delete', args=[new_user.id]))


        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:index'))


        with self.assertRaises(User.DoesNotExist):
            new_user.refresh_from_db()


        messages_list = list(response.wsgi_request._messages)
        self.assertTrue(
            any("успешно удален" in str(msg) for msg in messages_list),
            "Сообщение 'удален' не найдено в messages"
        )