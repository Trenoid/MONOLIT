from urllib import response
from django.test import TestCase
from django.urls import reverse



class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('main:index')
        response = self.client.get(path)
        print(response)