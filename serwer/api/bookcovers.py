from bottle import get, post, delete,    request, route,put, response, auth_basic, route
from models.bookcovers import BookCovers
from models.admins import Admins
import json

from api.cors import enable_cors

@route('/bookcovers', method=['OPTIONS', 'GET'])
# @get('/bookcovers')
@enable_cors
def bookscoverslist():
    return BookCovers.getAll()



@route('/bookcovers/<bookid>', method=['OPTIONS', 'GET'])
# @get('/bookcovers/<bookid>')
@enable_cors
def bookid(bookid):
    return BookCovers.getByIdOfBook(bookid)



#409 already exists cover for this book
#400 invalid request or no such book id in books collection
#201 success
@route('/bookcovers/<bookid>', method=['OPTIONS', 'POST'])
# @post('/bookcovers/<bookid>')
@enable_cors
@auth_basic(Admins.isCredentialsValid)
def createbybookid(bookid):
    try:
        bdata = request.body.read()
        response.status  = BookCovers.createByIdOfBook(bookid, bdata)
    except:
        response.status = 400


#400 no such id, invalid request or sth else
@route('/bookcovers/<bookid>', method=['OPTIONS', 'DELETE'])
# @delete('/bookcovers/<bookid>')
@enable_cors
@auth_basic(Admins.isCredentialsValid)
def deletebybookid(bookid):
    try:
        return BookCovers.deleteById(bookid)
    except:
        response.status = 400
