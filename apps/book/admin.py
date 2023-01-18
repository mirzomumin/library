from django.contrib import admin

from .models import Author, Category, Book


# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
