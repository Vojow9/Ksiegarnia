from bottle import get, post, delete,    request, route,put, response, auth_basic
from models.bookcovers import BookCovers
from models.admins import Admins
import json

from api.cors import enable_cors


@get('/bookcovers')
@enable_cors
def bookscoverslist():
    return BookCovers.getAll()

@get('/bookcovers/<bookid>')
@enable_cors
def bookid(bookid):
    return BookCovers.getByIdOfBook(bookid)

#409 already exists cover for this book
#400 invalid request or no such book id in books collection
#201 success
@post('/bookcovers/<bookid>')
@enable_cors
@auth_basic(Admins.isCredentialsValid)
def createbybookid(bookid):
    try:
        bdata = request.body.read()
        response.status  = BookCovers.createByIdOfBook(bookid, bdata)
    except:
        response.status = 400


#400 no such id, invalid request or sth else
@delete('/bookcovers/<bookid>')
@enable_cors
@auth_basic(Admins.isCredentialsValid)
def deletebybookid(bookid):
    try:
        return BookCovers.deleteById(bookid)
    except:
        response.status = 400
