from rest_framework.test import APITestCase
from django.urls import reverse


class CategoryTests(APITestCase):
	'''Tests for Category endpoints'''

	fixtures = ('categories.json',)

	def test_get_category_list(self):
		'''Test of getting all categories'''
		response = self.client.get(reverse('category_list'))
		self.assertEqual(response.status_code, 200)

	def test_update_category_name(self):
		'''Test of updating specific category name'''
		url = reverse('category_update', kwargs={"category_id": 58})
		data = {
			'name': 'Non-Fictions'
		}
		response = self.client.patch(url, data)
		self.assertEqual(response.status_code, 200)