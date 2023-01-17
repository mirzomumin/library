from rest_framework import serializers

from book.models import Book
from .author import AuthorSerializer
from .category import CategorySerializer


class BookListSerializer(serializers.ModelSerializer):
	authors = AuthorSerializer(many=True)
	class Meta:
		model = Book
		fields = ('id', 'name', 'authors', 'price')


class BookDetailSerializer(serializers.ModelSerializer):
	categories = CategorySerializer(many=True)
	authors = AuthorSerializer(many=True)
	class Meta:
		model = Book
		fields = ('id', 'name', 'description', 'price', 'categories', 'authors')


class BookUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Book
		fields = ('id', 'name', 'description', 'price', 'categories', 'authors')