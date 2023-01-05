from django.urls import path

from .views import BookListView


urlpatterns = [
    path('', BookListView, name='book_list.html')
]
