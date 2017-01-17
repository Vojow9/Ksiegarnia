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
@put('/customers')
def createCustomer():
    try:
        data = request.body.readlines()[0]
        response.status = Customers.createCustomer(data)
    except:
        response.status = 400
