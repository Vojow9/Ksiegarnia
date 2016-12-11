from django.shortcuts import render
from django.utils import timezone
from .models import Book
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

def book_list(request):
    books = Book.objects.all
    return render(request, 'sklep/book_list.html', {'books':books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'sklep/book_detail.html', {'book': book})

def shop_detail(request):
	return render(request, 'sklep/shop_detail.html')

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('sklep/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('sklep/loggedin.html',
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('sklep/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('sklep/logout.html')


def register_user(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResonseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()

    return render_to_response('sklep/register.html', args)

def register_success(request):
    return render_to_response('sklep/register_success.html')
