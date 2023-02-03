from django import forms

from .models import Book, Comment


class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'price']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', "recommend")
