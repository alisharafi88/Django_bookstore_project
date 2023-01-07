from django.urls import path

from . import views


urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list.html'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]
