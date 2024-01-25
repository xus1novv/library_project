from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import BookSerializer
from rest_framework import generics, status
from .models import Book

# Datalarni faqat List ko'rinishida chiqarib beradi
# class BookListAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# Tanlangan data ni chiqaradi faqat 1 tasini
# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#Tanlangan data ni o'chiradi
# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#Tanlangan data ni yangilaydi
# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# data yaratadi
# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListApiView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status":f"Returned {len(books)} books",
            "books":serializer_data
        }

        return Response(data)


class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                "status":"Books are successfull created",
                "Books":data
            }
            return Response(data)
        else:
            return Response(
                {
                    'status':"False",
                    'message':"Serializer is not valid"
                },
                status = status.HTTP_400_BAD_REQUEST

            )


class BookDetailApiView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data

            data = {
                "status":"Successfull",
                'book':serializer_data
            }

            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    'status':"False",
                    'message':"Book is not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()

            return Response(
                {
                    "status":True,
                    "message":"Book are deleted"
                }
            )
        except Exception:
            return Response(
                {
                    "status":False,
                    "message":"Book is not found"
                }
            )


class BookUpdateApiView(APIView):

    def put(self,request, pk):
        book = get_object_or_404(Book.objects.all(), id = pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {
                "status":True,
                "message":"Succesfull update your data"
            },
            status=status.HTTP_200_OK
        )

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer