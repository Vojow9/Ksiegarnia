from bottle import get, post
from models.authors import Authors

@get('/authors')
def booklist():
    return Authors.getAll()

@get('/authors/<id>')
def booklist(id):
    return Authors.getById(id)
