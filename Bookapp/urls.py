from django.urls import path
from .views import BookListApiView, BookDetailApiView,\
BookUpdateApiView, BookDeleteApiView,BookCreateApiView,\
BookListCreateApiVeiw,BookUpdateDeleteApiView

urlpatterns = [
    path('books/', BookListApiView.as_view(), ),
    path('books/list-create/', BookListCreateApiVeiw.as_view()),
    path('books/update-delete/<int:pk>', BookUpdateDeleteApiView.as_view()),
    path('books/create/',BookCreateApiView.as_view()),
    path('books/<int:pk>/', BookDetailApiView.as_view()),
    path('books/<int:pk>/update', BookUpdateApiView.as_view()),
    path('books/<int:pk>/delete', BookDeleteApiView.as_view()),
    # path('books/', book_api_view),
]