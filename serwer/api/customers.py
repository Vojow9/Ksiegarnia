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



@post('/customers/availablebooks/<id>')
@auth_basic(Customers.isCredentialsValid)
def customerslist(id):
    books = request.body.readlines()[0]
    response.status =  Customers.buyBooks(id,books)
# @post('/customers/<id>/availabebooks')
# @auth_basic(Customers.isCredentialsValid)
# def buybooks(id):
#     return Customers.getAllBooks(id)
