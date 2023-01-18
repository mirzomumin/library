from rest_framework import serializers

from book.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    '''Serializer of Author object'''

    class Meta:
        model = Author
        fields = ('id', 'name')
