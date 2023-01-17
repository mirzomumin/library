from rest_framework.test import APITestCase
from django.urls import reverse


class BookTests(APITestCase):
	'''Tests for Book endpoints'''

	fixtures = ('books.json', 'authors.json', 'categories.json')

	def test_get_book_list(self):
		'''Test of getting all books from library'''
		response = self.client.get(reverse('book_list'))
		self.assertEqual(response.status_code, 200)

	def test_get_detail_book_info(self):
		'''Test of getting specific book info'''
		url = reverse('book_detail', kwargs={"book_id": 155})
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_update_book_info(self):
		'''Test of updating specific book info'''
		url = reverse('book_detail', kwargs={"book_id": 155})
		data = {
			'name': 'Harry Potter and the Prisoner of Azkaban',
			'price': "20.99",
			'description': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
			'categories': [56, 59, 71],
			'authors': [155, 178]
		}
		response = self.client.put(url, data)
		self.assertEqual(response.status_code, 200)