from django.shortcuts import render
from django.utils import timezone
from .services import getBooksList, getBookById, getAuthorsList, getAuthorById, getBook, getBookCoverById
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from requests.auth import HTTPBasicAuth
import requests
import json


def login_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    context = {}
    if len(username) > 0 and len(password) > 0:
        login = requests.get('http://localhost:8080/customers/'+username,
                             auth=(username, password))
        if login.status_code == 200:
            # User podal poprawne dane, mozna stworzyc sesje
            login = json.loads(login.text)
            request.session['username'] = login['username']
            request.session['first_name'] = login['first_name']
            request.session['books'] = login['books']
            request.session['cart'] = []
            return HttpResponseRedirect('/')
    return render(request, 'sklep/login.html', context=context)


def logout_user(request):
    request.session.flush()
    return HttpResponseRedirect('/')


def add_to_cart(request, pk):
    if 'username' in request.session:
        cart = request.session['cart']
        cart.append(pk)
        request.session['cart'] = cart
        return new_cart(request)
    else:
        return HttpResponseRedirect('/')


def remove_from_cart(request, pk):
    if 'username' in request.session:
        if pk in request.session['cart']:
            request.session['cart'].remove(pk)
        return new_cart(request)
    else:
        return HttpResponseRedirect('/')


def new_cart(request):
    if 'username' in request.session:
        cart = request.session['cart']
        total = 0
        books = getBooksList()
        av = list()
        for book in books:
            url = "media/" + getBookCoverById(book['id']) + ".jpg"
            if book['isEbook'] == True or int(book['availability']) > 0:
                av.append(book)
            if book['id'] in cart:
                total = total + float(book['price'])
        return render(request, 'sklep/new_cart.html', {'books':av, 'url':url, 'total': total})
    return HttpResponseRedirect('/accounts/login')


def checkout(request):
    if 'username' in request.session:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        context = {}
        if len(username) > 0 and len(password) > 0:
            login = requests.get('http://localhost:8080/customers/' + username,
                                 auth=(username, password))
            if login.status_code == 200:
                cart = request.session['cart']
                books = request.session['books']
                books = books + cart
                url = "http://localhost:8080/customers/availablebooks/" + username
                for book in cart:
                    book_id = str(book)
                    requests.post(url, auth=HTTPBasicAuth(username, password), json = [book_id])
                request.session['books'] = books
                request.session['cart'] = []
                return mybooks(request)

        return render(request, 'sklep/checkout.html', {'status': 'Potwierdz swoje dane, aby sfinalizować transakcję'})

    return HttpResponseRedirect('/')

def mybooks(request):
    if 'username' in request.session:
        total = 0
        books = getBooksList()
        av = list()
        for book in books:
            url = "media/" + getBookCoverById(book['id']) + ".jpg"
            if book['isEbook'] == True or int(book['availability']) > 0:
                av.append(book)
        return render(request, 'sklep/mybooks.html', {'books':av, 'url':url, 'total': total})
    return HttpResponseRedirect('/accounts/login')


def auth_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def book_list(request):
	books = getBooksList()
	av = list()
	for book in books:
		url = "media/"+getBookCoverById(book['id'])+".jpg"
		if book['isEbook'] == True or int(book['availability']) > 0:
			av.append(book)
	return render(request, 'sklep/book_list.html', {'books':av, 'url':url})

def book_detail(request, pk):
	book = getBookById(pk)
	url = "media/"+book['id']+".jpg"
	print(url)
	al = book['authors']
	an = list()
	for aut in al:
		an.append(getAuthorById(aut)['name'])

	return render(request, 'sklep/book_detail.html', {'book': book,'authors':an , 'url':url})

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
	authors = getAuthorsList()
	books = getBooksList()
	return render(request, 'sklep/add_book.html',{'authors':authors, 'books':books})

def add_author(request):
    return render(request, 'sklep/add_author.html')

def cart(request):
    return render(request,'sklep/cart.html')


def register_success(request):
    return render_to_response('sklep/register_success.html')



def register_user(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()

    return render_to_response('sklep/register.html', args)
