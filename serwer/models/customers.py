from models.model import Model
from passlib.hash import pbkdf2_sha256
import json
import re
from .DBItemIdParser import DBItemIdParser
from bson.json_util import dumps
from bson import ObjectId
import ast
from datetime import datetime, timedelta
from .DBItemIdParser import DBItemIdParser


import models.books


class Customers(Model):

    collection = Model.db.customers

    def isValidUserForm(user):
        try:
            user = json.loads(str(user,'utf8'))
            for o in (user["username"], user["username"],
             user["password"], user["first_name"], user["email"]):
                if not Model.properLenOfObject(o):
                    print(o)
                    assert False
            m = re.match('^[0-9a-zA-Z]+$',user["username"])
            if not m:
                assert False
            if not Model.properLenOfObject(user["address"], max_len = 60):
                assert False
            if not '@' in user["email"]:
                assert False
            if (not 'Female' in user["gender"]) and (not "Male" in user["gender"]):
                assert False
            return True
        except:
            return False


    def createCustomer(new_user):
        if not Customers.isValidUserForm(new_user):
            return 400
        new_user = json.loads(str(new_user,'utf8'))
        if Customers.isValueUsed("username",new_user['username']):
            return 409
        new_user['password'] = pbkdf2_sha256.hash(new_user['password'])
        new_user['books'] = []
        Customers.collection.insert_one(new_user)
        return 201


    def UpdatePasswd(custid , passwdData):
        passwdData = json.loads(str(passwdData,'utf8'))
        passwd = passwdData['password']
        passwd = pbkdf2_sha256.hash(passwd)
        Customers.collection.update_one({'_id':ObjectId(custid)}, {"$set":{'password':passwd}})
        return 201



    def isCredentialsValid(username, password):
        try:
            hash = Customers.collection.find_one({'username':username})['password']
            return pbkdf2_sha256.verify(password,hash)
        except:
            return False

    #overrides Model.getById in order not to send a password
    def getById(id):
        collection = Customers.collection.find_one({'_id' :ObjectId(id)})
        collection = DBItemIdParser.prettyIdRepresentation(collection)
        del collection['password']
        return dumps(collection,ensure_ascii=False,).encode("utf8")


    def getByUsername(username):
        collection = Customers.collection.find_one({'username' :username})
        collection = DBItemIdParser.prettyIdRepresentation(collection)
        del collection['password']
        return dumps(collection,ensure_ascii=False,).encode("utf8")



    def getAllBooks(username):
        books = Customers.collection.find_one({'username' : username})['books']
        for i in range(len(books)):
            books[i]['bookid'] = str(books[i]['bookid'])
            books[i]['purchasedate'] = str(books[i]['purchasedate'])
            try:
                expdate = books[i]['expdate']
                books[i]['expired'] = False if expdate > datetime.now() else True
                books[i]['expdate'] = str(expdate)
            except KeyError:
                pass
        return dumps(books,ensure_ascii=False,).encode("utf8")

    def buyBooks(username,books):
        books = ast.literal_eval(str(books,'utf-8')) #conerts to python list with strings
        id = str(Customers.collection.find_one({'username':username})['_id'])
        if len(books) == 0:
            return 400
        if not models.books.Books.isBooksIdsValidId(books):
            return 400
        if not models.books.Books.isBooksAvailable(books):
            return 403
        if models.books.Books.isMoreThanOneEbook(books):
            return 403
        if Customers.isEbookAlreadyRented(id, books):
            return 403
        for bookid in books:
            new_book  = {'bookid':ObjectId(bookid),
                    'purchasedate':datetime.now(),
                    }
            if models.books.Books.isEbook(bookid):
                new_book['expdate'] = datetime.now() + timedelta(days=30)
                new_book['expired'] = False
            Customers.collection.update({'_id': ObjectId(id)}, {'$push': {'books': new_book}})
        models.books.Books.decreaseAvailability(books)
        return 201




    def isEbookAlreadyRented(customerid, bookslist):
        bookslist = [ObjectId(bookid) for bookid in bookslist]
        customers_owned_books = Customers.collection.find_one({'_id':ObjectId(customerid)})['books']
        customers_owned_ebooks = [b['bookid'] for b in customers_owned_books if 'expdate' in list(b)]
        intersection = [b for b in bookslist if b in customers_owned_ebooks]
        if len(intersection)>0:
            return True
