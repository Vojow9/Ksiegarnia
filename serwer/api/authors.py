from bottle import get, post, put, delete,  auth_basic, response, request
from models.authors import Authors
from models.books import Books
from models.admins import Admins

from api.cors import enable_cors

@get('/authors')
@enable_cors
def authorslist():
    return Authors.getAll()




@get('/authors/<id>')
@enable_cors
def author(id):
    return Authors.getById(id)



#name must be unique
#409 if name of author is already used
#400 invaild form
#201 succes, author created
@post('/authors')
@enable_cors

def createAuthor():
    try:
        data = request.body.readlines()[0]
        response.status = Authors.createAuthor(data)
    except:
        response.status = 400


#403 if author is author is in any book yet
#200 success
#400 wrong id form
#404 no such author id in db
@delete('/authors/<id>')
@enable_cors
@auth_basic(Admins.isCredentialsValid)
def deleteauthor(id):
    try:
        response.status =  Authors.deleteById(id)
    except:
        response.status = 400
