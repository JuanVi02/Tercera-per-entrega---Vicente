from django.shortcuts import render, redirect
from .models import Author, Category, Book
from .forms import AuthorForm, CategoryForm, BookForm
from django.db.models import Q

# Vista para insertar datos de autor
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_author')
    else:
        form = AuthorForm()
    return render(request, 'app/add_author.html', {'form': form})

# Vista para insertar datos de categoría
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = CategoryForm()
    return render(request, 'app/add_category.html', {'form': form})

# Vista para insertar datos de libro
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')
    else:
        form = BookForm()
    return render(request, 'app/add_book.html', {'form': form})

# Vista para buscar libros por título o autor
def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(
        Q(title__icontains=query) | Q(author__name__icontains=query)
    )
    return render(request, 'app/search_books.html', {'books': books, 'query': query})