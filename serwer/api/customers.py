from bottle import get, post, request, route,put, response, auth_basic
from models.customers import Customers
import json

@get('/customers')
def customerslist():
    return Customers.getAll()


@get('/customers/<username>')
@auth_basic(Customers.isCredentialsValid)
def customer(username):
    return Customers.getByUsername(username)


@put('/customers')
def createCustomer():
    try:
        data = request.body.readlines()[0]
        response.status = Customers.createCustomer(data)
    except:
        response.status = 400
