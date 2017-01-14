from bottle import get, post, request, route,put, response
from models.books import Books
import json

@get('/books')
def bookslist():
    return Books.getAll()

@get('/books/<id>')
def book(id):
    return Books.getById(id)


@put('/books')
def createBook():
    data = request.body.readlines()[0]
    response.status = Books.createBook(data)
