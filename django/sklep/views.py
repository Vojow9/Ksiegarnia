from django.shortcuts import render
from django.utils import timezone
from .services import getBooksList, getBookById, getAuthorsList, getAuthorById, getBook
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm



def book_list(request):
	books = getBooksList()
	av = list()
	for book in books:
		if book['isEbook'] == True or int(book['availability']) > 0:
			av.append(book)
	return render(request, 'sklep/book_list.html', {'books':av})

def book_detail(request, pk):
    book = getBookById(pk)
    al = book['authors']
    an = list()
    for aut in al:
        an.append(getAuthorById(aut)['name'])
        print(an)

    return render(request, 'sklep/book_detail.html', {'book': book,'authors':an})

def book(request):
    books = getBook()
    return render(request, 'sklep/book.html', {'books':books})

def author_list(request):
    authors = getAuthorsList()
    return render(request, 'sklep/author_list.html', {'authors':authors})

def author_detail(request, pk):
    author = getAuthorById(pk)
    return render(request, 'sklep/author_detail.html', {'author': author})

def shop_detail(request):
	return render(request, 'sklep/shop_detail.html')

def add_book(request):
    return render(request, 'sklep/add_book.html')

def add_author(request):
    return render(request, 'sklep/add_author.html')

def cart(request):
    return render(request,'sklep/cart.html')
