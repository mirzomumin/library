from django.urls import path

from book.views.book import BookListAPIView, BookDetailAPIView
from book.views.author import AuthorListAPIView, AuthorUpdateAPIView
from book.views.category import CategoryListAPIView, CategoryAPIView


urlpatterns = [

	# Book
	path('all/', BookListAPIView.as_view(), name='book_list'),
	path('<int:book_id>/', BookDetailAPIView.as_view(), name='book_detail'),

	# Author
	path('authors/all/', AuthorListAPIView.as_view(), name='author_list'),
	path('authors/<int:author_id>/', AuthorUpdateAPIView.as_view(),
		name='author_update'),

	# Category
	path('categories/all/', CategoryListAPIView.as_view(), name='category_list'),
	path('categories/<int:category_id>/', CategoryAPIView.as_view(),
		name='category_update')
]