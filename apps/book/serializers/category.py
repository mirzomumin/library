from rest_framework import serializers

from book.models import Category, Author, Book


class CategorySerializer(serializers.ModelSerializer):
    '''Serializer of Category'''

    class Meta:
        model = Category
        fields = ('id', 'name')
