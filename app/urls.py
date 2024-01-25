from django.urls import path
from .views import BookListApiView, BookCreateApiView,BookDetailApiView,BookDeleteApiView, BookViewSet
from rest_framework.routers import SimpleRouter

# router = SimpleRouter()
# router.register('books', BookViewSet, basename='books')
urlpatterns = [
    path('books/', BookListApiView.as_view()),
    path('books/create/', BookCreateApiView.as_view(), name = 'book_create_api'),
    path('books/<int:pk>/',BookDetailApiView.as_view(), name = 'book_detail_api'),
    # path('books/<int:pk>/update', BookUpdateApiView.as_view(), name = 'book_update_api'),
    path('books/<int:pk>/delete', BookDeleteApiView.as_view(), name = 'book_delete_api'),
    # path('books', book_list_view, name = 'book_list_api'),

]
#
# urlpatterns = urlpatterns + router.urls