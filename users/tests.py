from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import User
from .models import Status

User = get_user_model()

class UserCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        self.admin = User.objects.create_superuser(
            username='admin',
            password='adminpassword123'
        )

    def test_user_create_view_get(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/create.html')

    def test_user_create_success(self):
        response = self.client.post(reverse('user_create'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com'
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_update_view_get(self):
        self.client.login(username='admin', password='adminpassword123')
        response = self.client.get(reverse('user_update', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/update.html')

    def test_user_update_post(self):
        self.client.login(username='admin', password='adminpassword123')
        response = self.client.post(reverse('user_update', args=[self.user.id]), {
            'username': 'updateduser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com'
        }, follow=True)

        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

    def test_user_delete_view_get(self):
        self.client.login(username='admin', password='adminpassword123')
        response = self.client.get(reverse('user_delete', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/delete.html')

    def test_user_delete_view_post(self):
        self.client.login(username='admin', password='adminpassword123')
        response = self.client.post(reverse('user_delete', args=[self.user.id]), follow=True)
        with self.assertRaises(User.DoesNotExist):
            self.user.refresh_from_db()


    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_success(self):
        url = reverse('login')
        response = self.client.post(url, {
            'username': 'testuser',
            'password': 'testpassword123'
        }, follow=True)

        self.assertRedirects(response, reverse('user_create'))

    def test_logout_view_post(self):
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.post(reverse('logout'), follow=True)
        self.assertRedirects(response, reverse('home'))


class StatusCRUDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_status_list_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 200)

    def test_status_create_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('status_create'), {'name': 'В работе'}, follow=True)
        self.assertRedirects(response, reverse('statuses'))

    def test_status_update_view(self):
        status = Status.objects.create(name='Новый')
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('status_update', args=[status.id]), {
            'name': 'В работе',
        }, follow=True)
        status.refresh_from_db()
        self.assertEqual(status.name, 'В работе')

    def test_status_delete_view(self):
        status = Status.objects.create(name='Завершен')
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('status_delete', args=[status.id]), follow=True)
        with self.assertRaises(Status.DoesNotExist):
            status.refresh_from_db()

    def test_status_delete_protected(self):
        status = Status.objects.create(name='В работе')
        task = Task.objects.create(
            name='Задача',
            status=status,
            created_by=self.user
        )
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('status_delete', args=[status.id]), follow=True)
        self.assertContains(response, 'Невозможно удалить статус, который используется в задачах')