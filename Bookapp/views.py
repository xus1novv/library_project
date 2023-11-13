from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import Bookserializers
from rest_framework import generics, status


# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Bookserializers

class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = Bookserializers(books, many=True).data
        data = {
            'status':f"Returned {len(books)} books",
            'books':serializer_data
        }
        return Response(data)



# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Bookserializers


class BookDetailApiView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = Bookserializers(book).data

            data = {
                'status':'True',
                'book':serializer_data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {'status':'False', 'message':'Book is not found'},
                status=status.HTTP_404_NOT_FOUND
            )




# class BookDelateApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Bookserializers

class BookDeleteApiView(APIView):

    def delete(self,request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response(
                {'status':True, 'msg':'Successfull'},
                status=status.HTTP_200_OK

            )
        except Exception:
            return Response(
            {'status':False, 'msg':'Book is not found'},
                status=status.HTTP_404_NOT_FOUND
            )

# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Bookserializers

class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = Bookserializers(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {'status':'True', 'msg':'Book successfull update'},
            status=status.HTTP_200_OK
        )

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Bookserializers

class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = Bookserializers(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'status':f"Books are saved to the database",
                'books':data
            }
            return Response(data)


class BookListCreateApiVeiw(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializers

class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializers

# @api_view(['GET'])
# def book_api_view(request, *args, **kwargs):
#     books = Book.objects.all()
#     serializers = Bookserializers(books, many=True)
#     return Response(serializers.data)
