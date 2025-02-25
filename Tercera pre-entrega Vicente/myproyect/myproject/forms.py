from django import forms
from .models import Author, Category, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'publication_date']