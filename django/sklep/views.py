from django.shortcuts import render
from django.utils import timezone
from .models import Book
from django.shortcuts import render, get_object_or_404

def book_list(request):
    books = Book.objects.all
    return render(request, 'sklep/book_list.html', {'books':books})
	
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'sklep/book_detail.html', {'book': book})

def shop_detail(request):
	return render(request, 'sklep/shop_detail.html')