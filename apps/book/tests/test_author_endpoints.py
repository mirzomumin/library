from rest_framework.test import APITestCase
from django.urls import reverse


class AuthorTests(APITestCase):
	'''Tests for Author endpoints'''

	fixtures = ('authors.json',)

	def test_get_author_list(self):
		'''Test of getting all authors'''
		response = self.client.get(reverse('author_list'))
		self.assertEqual(response.status_code, 200)

	def test_update_author_name(self):
		'''Test of updating specific author name'''
		url = reverse('author_update', kwargs={"author_id": 153})
		data = {
			'name': 'Charles Dickens'
		}
		response = self.client.patch(url, data)
		self.assertEqual(response.status_code, 200)