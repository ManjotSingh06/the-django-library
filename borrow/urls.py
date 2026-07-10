from django.urls import path
from .views import borrow_book


urlpatterns = [
    path('borrow/<int:pk>/', borrow_book, name="borrow-book"),
]