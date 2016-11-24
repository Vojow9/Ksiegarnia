from bottle import get, post
from models.authors import Authors

@get('/authors')
def booklist():
    return Authors.getAll()

'''
@get('/books/allIdAndTitles')
def booklist():
    return models.Books.getAllIdAndTittles()
'''

@get('/authors/<id>')
def booklist(id):
    return Authors.getById(id)
