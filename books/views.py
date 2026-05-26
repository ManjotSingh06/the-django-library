

from django.views.generic import ListView, DetailView
from django.db.models import Q  
from .models import Book
from django.contrib import messages 

from rest_framework.generics import ListAPIView
from .serializers import BookSerializer


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
         query = self.request.GET.get('q')
         if query:
             return Book.objects.filter(
                 Q(title__icontains=query) |
                 Q(author__icontains=query)
             )
         return Book.objects.all()

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer