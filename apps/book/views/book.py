from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from drf_yasg.utils import swagger_auto_schema

from book.serializers.book import (
    BookListSerializer,
    BookDetailSerializer,
    BookCreateUpdateSerializer
)
from book.models import Book


# Create your views here.


class BookListAPIView(ListAPIView):
    '''Get all books in the library'''
    serializer_class = BookListSerializer
    queryset = Book.objects.all().prefetch_related('authors')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'authors__name']


class BookDetailAPIView(APIView):
    """
    Retrieve and update book instance.
    """

    @swagger_auto_schema(responses={200: BookDetailSerializer(many=False)})
    def get(self, request, book_id):
        '''Get full info about selected book'''
        book = get_object_or_404(Book, id=book_id)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data, status=HTTP_200_OK)

    @swagger_auto_schema(request_body=BookCreateUpdateSerializer)
    def put(self, request, book_id):
        '''Update selected book'''
        book = get_object_or_404(Book, id=book_id)
        serializer = BookCreateUpdateSerializer(book, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class BookCreateAPIView(APIView):
    """
    Create book instance.
    """

    @swagger_auto_schema(request_body=BookCreateUpdateSerializer)
    def post(self, request):
        '''Create a new book'''
        serializer = BookCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)