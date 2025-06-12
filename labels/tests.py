from django.test import TestCase
from django.urls import reverse
from .models import Label


class LabelCRUDTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.label = Label.objects.create(name='bug')

    def test_label_creation(self):
        response = self.client.post(reverse('labels:create'), {
            'name': 'feature'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Label.objects.filter(name='feature').exists())

    def test_label_update(self):
        response = self.client.post(reverse('labels:update', args=[self.label.id]), {
            'name': 'feature_label'
        })
        self.assertEqual(response.status_code, 302)
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'feature_label')

    def test_label_deletion(self):
        response = self.client.post(reverse('labels:delete', args=[self.label.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Label.objects.filter(id=self.label.id).exists())