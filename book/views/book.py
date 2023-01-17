from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes
from drf_yasg.utils import swagger_auto_schema

from book.serializers.book import (
	BookListSerializer,
	BookDetailSerializer,
	BookUpdateSerializer
)
from book.models import Book
# Create your views here.


class BookListAPIView(ListAPIView):
	'''Get all books in the library'''
	serializer_class = BookListSerializer
	queryset = Book.objects.all().prefetch_related('author')
	filter_backends = [filters.SearchFilter]
	search_fields = ['name', 'author__name']


class BookDetailAPIView(APIView):
	"""
	Retrieve and update book instance.
	"""

	@swagger_auto_schema(responses={200: BookDetailSerializer(many=False)})
	def get(self, request, book_id):
		'''Get full info about selected book'''
		book = get_object_or_404(Book, id=book_id)
		serializer = BookDetailSerializer(book)
		return Response(serializer.data)

	@parser_classes(MultiPartParser,)
	@swagger_auto_schema(request_body=BookUpdateSerializer)
	def put(self, request, book_id):
		'''Update selected book'''
		book = get_object_or_404(Book, id=book_id)
		serializer = BookUpdateSerializer(book, data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)