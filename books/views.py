from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.

from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, "books/index.html", {
        "books": books
    })


def book_details(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404
    
    book = get_object_or_404(Book, slug=slug)   # does same as above

    return render(request, "books/book_details.html", {
        "title": book.title,
        "rating": book.rating,
        "author": book.author,
        "is_bestseller": book.is_best_selling
    })