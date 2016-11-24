import json, pymongo
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps


class Model():
    def connect_to_database(host='localhost', port=27017):
        client = MongoClient(host, port)
        db = client.ksiegarniadb
        return db

    db = connect_to_database()

    @classmethod
    def getAll(cls):
        return dumps(cls.collection.find())

    @classmethod
    def getById(cls,id):
        return dumps(cls.find_one({'_id' :ObjectId(id)}))
