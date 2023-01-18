from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from drf_yasg.utils import swagger_auto_schema

from book.serializers.category import (
    CategorySerializer
)
from book.models import Category


# Create your views here.


class CategoryAPIView(APIView):
    '''Update category instance'''

    @swagger_auto_schema(request_body=CategorySerializer)
    def patch(self, request, category_id):
        '''Update selected category'''
        category = get_object_or_404(Category, id=category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CategoryListAPIView(ListCreateAPIView):
    '''Get list of all book categories and create category instance'''

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
