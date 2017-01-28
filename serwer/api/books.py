from bottle import get, post, delete, request, route,put, response, auth_basic
from models.books import Books
from models.admins import Admins
import json

from api.cors import enable_cors


#teraz zostaje tylko do testowania, normalnie usune ze wzgledow bezpieczenstwa
@get('/books')
@enable_cors
def bookslist():
    return Books.getAll()

@get('/books/<id>')
@enable_cors
def book(id):
    return Books.getById(id)



#return all books written by an author
@get('/books/author/<id>')
@enable_cors
def book(id):
    return Books.getAllOfAuthor(id)

#ISBN must be unique
#409 if ISBN already in db
#400 invalid request form or sth else
#201 success
@post('/books')
@enable_cors
@auth_basic(Admins.isCredentialsValid)
def createBook():
    try:
        data = request.body.readlines()[0]
        response.status = Books.createBook(data)
    except:
        response.status = 400


# update availabity
# send { 'availabity':10}
@put('/books/<id>')
@enable_cors
@auth_basic(Admins.isCredentialsValid)
def uptdAvailability(id):
    try:
        data = request.body.readlines()[0]
        response.status = Books.UpdateAvailability(id,data)
    except:
        response.status = 400


#404 boo id k not in db
#400 invalid id form or sth else
#200 success
@delete('/books/<id>')
@enable_cors
@auth_basic(Admins.isCredentialsValid)
def deletebyid(id):
    try:
        response.status = Books.deleteById(id)
    except:
        response.status = 400
