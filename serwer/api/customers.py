from bottle import get, post, request, route,put, response
from models.customers import Customers
import json

@get('/customers')
def customerslist():
    return Customers.getAll()

@get('/customers/<id>')
def customer(id):
    return Customers.getById(id)


@put('/customers')
def createCustomer():
    data = request.body.readlines()[0]
    response.status = Customers.createCustomer(data)
