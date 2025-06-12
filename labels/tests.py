from django.test import TestCase
from .forms import LabelForm
from .models import Label
from users.models import User
from django.urls import reverse

class LabelCRUDTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass123')
        cls.label = Label.objects.create(name='bug')

    def setUp(self):
        self.client.force_login(self.user)

    def test_label_creation(self):
        data = {'name': 'new_feature'}
        form = LabelForm(data=data)

        self.assertTrue(form.is_valid())

        form.save()

        self.assertTrue(Label.objects.filter(name='new_feature').exists())

    def test_label_update(self):

        self.client.login(username='testuser', password='testpass123')  # замени на твои фикстуры
        response = self.client.post(
            reverse('labels:update', args=[self.label.id]),
            {'name': 'updated_name'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('labels:index'))
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'updated_name')



    def test_label_deletion(self):
        response = self.client.post(reverse('labels:delete', args=[self.label.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Label.objects.filter(id=self.label.id).exists())