from django.urls import path
from .views import borrow_book, return_book


urlpatterns = [
    path('borrow/<int:pk>/', borrow_book, name="borrow-book"),
    path('return/<int:pk>/',return_book, name="return-book"),
]