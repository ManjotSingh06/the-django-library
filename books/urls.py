from django.urls import path
from .views import BookListAPIView, BookListView, BookDetailView , BookCreateView

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('api/books/', BookListAPIView.as_view()),
    path('add/', BookCreateView.as_view(), name='book-add'),
]