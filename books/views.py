from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models import Avg # For Aggregation
# Create your views here.

from .models import Book

def index(request):
    books = Book.objects.all().order_by("-title")   # orders by data; minus is desc
    num_books = books.count()
    avg_rate = books.aggregate(Avg("rating")) 
    
    return render(request, "books/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "average_rate": avg_rate
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