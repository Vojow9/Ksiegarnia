from bottle import get, post, request, route,put, response, auth_basic
from models.books import Books
from models.admins import Admins
import json

@get('/books')
def bookslist():
    return Books.getAll()

@get('/books/<id>')
def book(id):
    return Books.getById(id)


@put('/books')
@auth_basic(Admins.isCredentialsValid)
def createBook():
    try:
        data = request.body.readlines()[0]
        response.status = Books.createBook(data)
    except:
        response.status = 400
