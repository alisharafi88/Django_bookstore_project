from django.contrib import admin

from .models import Book, Comment


@admin.register(Comment)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'datetime', 'text', 'recommend')


admin.site.register(Book)
