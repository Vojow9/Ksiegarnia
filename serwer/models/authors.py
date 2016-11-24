import json, pymongo
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps

def connect_to_database(host='localhost', port=27017):
    client = MongoClient(host, port)
    db = client.ksiegarniadb
    return db

db = connect_to_database()


class Authors():
    authors = db.authors
    def getAll():
        return dumps(Authors.authors.find())
    def getById(id):
        return dumps(Authors.authors.find_one({'_id' :ObjectId(id)}))
