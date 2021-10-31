# https://www.cnblogs.com/1204guo/p/8058449.html
# django_test

from rest_framework.test import APITestCase
from rest_framework import status


class BaseTest(APITestCase):
    def setUp(self):
        self.model = ""
        self.base_url = ""
        # self.base_url = "/api/domain/1/"
        # self.base_url = "/api/app/"
        self.data = ""

    def _create(self):
        data = self.data
        response = self.client.post(self.base_url, data, format='json')
        response = self.client.put(self.base_url, data, format='json')
        response = self.client.patch(self.base_url, data, format='json')
        response = self.client.get(self.base_url, format='json')
        response = self.client.delete(self.base_url, format='json')
        response.data

    def tearDown(self):
        self.model.objects.all().delete()
