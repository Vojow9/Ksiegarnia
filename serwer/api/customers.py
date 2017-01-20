from bottle import get, post, request, route,put, response, auth_basic
from models.customers import Customers
import json

@get('/customers')
def customerslist():
    return Customers.getAll()


@get('/customers/<id>')
@auth_basic(Customers.isCredentialsValid)
def customer(id):
    return Customers.getById(id)



#username must be unique
#400 invalid form
#409 username already in db
#201 success
@post('/customers')
def createCustomer():
    try:
        data = request.body.readlines()[0]
        response.status = Customers.createCustomer(data)
    except:
        response.status = 400


@get('/customers/availablebooks/<id>')
@auth_basic(Customers.isCredentialsValid)
def customerslist(id):
    return Customers.getAllBooks(id)


#request must be list of 'id' of books you want to buy/borrow
#for example:
#400 invalid request form or sth else
#403 ebook already rented by user
#201 success
@post('/customers/availablebooks/<id>')
@auth_basic(Customers.isCredentialsValid)
def customerslist(id):
    try:
        books = request.body.readlines()[0]
        response.status =  Customers.buyBooks(id,books)
    except:
        response.status = 400
