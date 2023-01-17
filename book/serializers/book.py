from rest_framework import serializers

from book.models import Book
from .author import AuthorSerializer
from .category import CategorySerializer


class BookListSerializer(serializers.ModelSerializer):
	author = AuthorSerializer(many=True)
	class Meta:
		model = Book
		fields = ('id', 'name', 'author', 'price')


class BookDetailSerializer(serializers.ModelSerializer):
	category = CategorySerializer(many=True)
	author = AuthorSerializer(many=True)
	class Meta:
		model = Book
		fields = ('id', 'name', 'description', 'price', 'category', 'author')


class BookUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Book
		fields = ('id', 'name', 'description', 'price', 'category', 'author')