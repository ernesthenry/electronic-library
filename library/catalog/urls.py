# Use include() to add paths from the catalog application
from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/catalog', views.BookListView.as_view(), name='books'),
    path('book/catalog/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]

urlpatterns += [
    path('catalog/mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('catalog/borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),  # Added for challenge
    path('catalog/book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
