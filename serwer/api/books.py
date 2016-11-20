from bottle import get, post
import models

@get('/books/all')
def booklist():
    return models.Books.getAllIdAndTittles()

@get('/books/allIdAndTitles')
def booklist():
    return models.Books.getAllIdAndTittles()

@get('/books/<id>')
def booklist(id):
    return models.Books.getBookById(id)
