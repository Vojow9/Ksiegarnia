from bottle import get, post, put, delete,  auth_basic, response, request
from models.authors import Authors
from models.admins import Admins

@get('/authors')
def authorslist():
    return Authors.getAll()

@get('/authors/<id>')
def author(id):
    return Authors.getById(id)

#name must be unique
@post('/authors')
@auth_basic(Admins.isCredentialsValid)
def createAuthor():
    try:
        data = request.body.readlines()[0]
        response.status = Authors.createAuthor(data)
    except:
        response.status = 400


#403 if author is author in any book
@delete('/authors/<id>')
@auth_basic(Admins.isCredentialsValid)
def deleteauthor(id):
    response.status =  Authors.deleteById(id)
