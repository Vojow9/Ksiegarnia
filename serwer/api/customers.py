from bottle import get, post, request, route,put, response, auth_basic, route
from models.customers import Customers
import json

from api.cors import enable_cors


#teraz zostaje tylko do testowania, normalnie usune ze wzgledow bezpieczenstwa
@route('/customers', method=['OPTIONS', 'GET'])
# @get('/customers')
@enable_cors
def customerslist():
    return Customers.getAll()


@route('/customers/<username>', method=['OPTIONS', 'GET'])
# @get('/customers/<username>')
@enable_cors
@auth_basic(Customers.isCredentialsValid)
def customer(username):
    return Customers.getByUsername(username)






# @get('/customers/<id>')
# @enable_cors
# @auth_basic(Customers.isCredentialsValid)
# def customer(id):
#     return Customers.getById(id)


# update pasword
# send { 'password':'abc}
@route('/customers/<id>', method=['OPTIONS', 'PUT'])
# @put('/customers/<id>')
@enable_cors
@auth_basic(Customers.isCredentialsValid)
def changepasswd(id):
    try:
        data = request.body.readlines()[0]
        response.status = Customers.UpdatePasswd(id,data)
    except:
        response.status = 400

#username must be unique
#400 invalid form
#409 username already in db
#201 success
@route('/customers', method=['OPTIONS', 'POST'])
# @post('/customers')
@enable_cors
def createCustomer():
    try:
        data = request.body.readlines()[0]
        response.status = Customers.createCustomer(data)
    except:
        response.status = 400


@route('/customers/availablebooks/<username>', method=['OPTIONS', 'GET'])
# @get('/customers/availablebooks/<username>')
@enable_cors
@auth_basic(Customers.isCredentialsValid)
def customerslist(username):
    return Customers.getAllBooks(username)


#request must be list of 'id' of books you want to buy/borrow
# if you want to buy two same books place it twice, for example : ["5836048f57aac220c4c87383", "5836048f57aac220c4c87383"]
#400 invalid request form or sth else
#403 ebook already rented by user or not enough books in shop
#403 you cannot rent more than one ebook
#403 if your  ebook is not expired, you cant rent this ebook
#201 success
@route('/customers/availablebooks/<username>', method=['OPTIONS', 'POST'])
# @post('/customers/availablebooks/<username>')
@enable_cors
@auth_basic(Customers.isCredentialsValid)
def customerslist(username):
    try:
        books = request.body.readlines()[0]
        response.status =  Customers.buyBooks(username,books)
    except:
        response.status = 400
