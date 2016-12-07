from sklep.models import Book
from rest.serializers import BookSerializer
from rest.serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'books': reverse('books-list', request=request, format=format)
    })

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserList(generics.ListAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer

# from rest_framework import status
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from sklep.models import Book
# from rest.serializers import BookSerializer
# from rest_framework import mixins
# from rest_framework import generics
#
#
# class BookList(APIView):
#     def get(self, request, format=None):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = BookSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # def delete(self, request, pk, format=None):
#     #     book = self.get_object(pk)
#     #     book.delete()
#     #     return Response(status=status.HTTP_204_NO_CONTENT)
#
# class BookDetail(APIView):
#     """
#     Retrieve, update or delete a book instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         book = self.get_object(pk)
#         book = BookSerializer(book)
#         return Response(book.data)
#
#     def put(self, request, pk, format=None):
#         book = self.get_object(pk)
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         book = self.get_object(pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)