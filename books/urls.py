from django.urls import path
from .views import Book_List, Category_list, Book_Detail, BookCreate, BookDelete, BookUpdate, Search_Book

urlpatterns = [
    path("", Book_List.as_view(), name="book_list"),
    path("<int:pk>/", Book_Detail.as_view(), name="book_detail"),
    path("category/<int:pk>/", Category_list.as_view(), name="category_list_book"),
    path("new/", BookCreate.as_view(), name="book_new"),
    path("delete/<int:pk>", BookDelete.as_view(), name="book_delete"),
    path("update/<int:pk>", BookUpdate.as_view(), name="book_update"),
    path("search/", Search_Book.as_view(), name='search_book'),
]
