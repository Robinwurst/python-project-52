from django.test import TestCase
from django.urls import reverse
from .models import Label


class LabelTest(TestCase):
    def setUp(self):
        self.label = Label.objects.create(name='Метка 1')

    def test_label_create(self):
        response = self.client.post(reverse('labels:create'), {
            'name': 'Метка 2'
        })

        print(response.status_code)
        print(response.content.decode())
        if 'form' in response.context:
            print(response.context['form'].errors) 

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Label.objects.filter(name='Метка 2').exists())

    def test_label_update(self):
        response = self.client.post(reverse('labels:update', args=[self.label.id]), {
            'name': 'Метка обновлена'
        })
        self.label.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.label.name, 'Метка обновлена')

    def test_label_delete(self):
        response = self.client.post(reverse('labels:delete', args=[self.label.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Label.objects.filter(id=self.label.id).exists())