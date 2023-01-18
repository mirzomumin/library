from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from drf_yasg.utils import swagger_auto_schema

from book.serializers.book import (
    AuthorSerializer,
)
from book.models import Author


# Create your views here.


class AuthorUpdateAPIView(APIView):
    '''Update author instance'''

    @swagger_auto_schema(request_body=AuthorSerializer)
    def patch(self, request, author_id):
        '''Update selected author'''
        author = get_object_or_404(Author, id=author_id)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class AuthorListAPIView(ListCreateAPIView):
    '''Get list of all book authors and create author instance'''

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
