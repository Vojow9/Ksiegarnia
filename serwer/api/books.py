from bottle import get, post, request, route,put
from models.books import Books
import json

@get('/books')
def booklist():
    return Books.getAll()

@get('/books/<id>')
def booklist(id):
    return Books.getById(id)


@put('/ser')
def update_handler():
    '''Handles name updates'''

    data = json.load(request.body.decode("utf-8"))
    print(data)
