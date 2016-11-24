from bottle import get, post
from models.books import Books

@get('/books')
def booklist():
    return Books.getAll()

@get('/books/<id>')
def booklist(id):
    return Books.getById(id)
