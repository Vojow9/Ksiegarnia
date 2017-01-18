from bottle import get, post, delete,    request, route,put, response, auth_basic
from models.bookcovers import BookCovers
from models.admins import Admins
import json

@get('/bookcovers')
def bookscoverslist():
    return BookCovers.getAll()

@get('/bookcovers/<bookid>')
def bookid(bookid):
    return BookCovers.getByIdOfBook(bookid)



@post('/bookcovers/<bookid>')
@auth_basic(Admins.isCredentialsValid)
def createbybookid(bookid):
    bdata = request.body.read()
    return BookCovers.createByIdOfBook(bookid, bdata)

@delete('/bookcovers/<bookid>')
@auth_basic(Admins.isCredentialsValid)
def deletebybookid(bookid):
    return BookCovers.deleteById(bookid)


# #ISBN must be unique
# @put('/books')
# @auth_basic(Admins.isCredentialsValid)
# def createBook():
#     try:
#         data = request.body.readlines()[0]
#         response.status = Books.createBook(data)
#     except:
#         response.status = 400
