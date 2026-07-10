from django.shortcuts import redirect, get_object_or_404
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from books.models import Book
from .models import Borrow

@login_required
def borrow_book(request, pk):

    book = get_object_or_404(Book, pk=pk)

    if book.available :
        
        Borrow.objects.create(
            user = request.user,
            book = book,
            due_date = timezone.now().date() + timedelta(days=14)
        )
        book.available = False
        book.save()

    return redirect('book-detail', pk=book.id)