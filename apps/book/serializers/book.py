from rest_framework import serializers

from book.models import Book
from .author import AuthorSerializer
from .category import CategorySerializer


class BookListSerializer(serializers.ModelSerializer):
    '''Book Serializer of list objects to get'''
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'authors', 'price')


class BookDetailSerializer(serializers.ModelSerializer):
    '''Book Serializer of detail object to get'''
    categories = CategorySerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'price', 'categories', 'authors')


class BookCreateUpdateSerializer(serializers.ModelSerializer):
    '''Book Serializer of detail object to update and create'''

    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'price', 'categories', 'authors')