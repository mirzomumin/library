from django.urls import path

from book.views.book import BookListAPIView, BookDetailAPIView, BookCreateAPIView
from book.views.author import AuthorListAPIView, AuthorUpdateAPIView
from book.views.category import CategoryListAPIView, CategoryAPIView

urlpatterns = [

    # Book
    path('all/', BookListAPIView.as_view(), name='book_list'),
    path('<int:book_id>/', BookDetailAPIView.as_view(), name='book_detail'),
    path('create/', BookCreateAPIView.as_view(), name='book_create'),

    # Author
    path('authors/', AuthorListAPIView.as_view(), name='author_list'),
    path('authors/<int:author_id>/', AuthorUpdateAPIView.as_view(),
         name='author_update'),

    # Category
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:category_id>/', CategoryAPIView.as_view(),
         name='category_update')
]
