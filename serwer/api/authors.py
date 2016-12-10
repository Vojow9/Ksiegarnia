from bottle import get, post
from models.authors import Authors

@get('/authors')
def authorslist():
    return Authors.getAll()

@get('/authors/<id>')
def authorslist(id):
    return Authors.getById(id)
