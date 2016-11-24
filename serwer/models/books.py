import json, pymongo
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps

def connect_to_database(host='localhost', port=27017):
    client = MongoClient(host, port)
    db = client.ksiegarniadb
    return db

db = connect_to_database()


class Books():
    books = db.books
    def getAllBooks():
        return dumps(Books.books.find())
    def getBookById(id):
        return dumps(Books.books.find_one({'_id' :ObjectId(id)}))
