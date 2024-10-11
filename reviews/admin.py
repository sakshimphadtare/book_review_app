from django.contrib import admin

from django.contrib import admin
from .models import Author, Book, Review

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'author__name')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('book__title',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)

