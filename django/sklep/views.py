from django.shortcuts import render
from django.utils import timezone
from .services import getBooksList, getBookById
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

def book_list(request):
    books = getBooksList()
    return render(request, 'sklep/book_list.html', {'books':books})

def book_detail(request, pk):
    book = getBookById(pk)
    return render(request, 'sklep/book_detail.html', {'book': book})

def shop_detail(request):
	return render(request, 'sklep/shop_detail.html')