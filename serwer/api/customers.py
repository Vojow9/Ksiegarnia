from bottle import get, post, request, route,put
from models.customers import Customers
import json

@get('/customers')
def customerslist():
    return Customers.getAll()

@get('/customers/<id>')
def customer(id):
    return Customers.getById(id)
