import json, pymongo
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps,default


class Model():
    def connect_to_database(host='localhost', port=27017):
        client = MongoClient(host, port)
        db = client.ksiegarniadb
        return db

    db = connect_to_database()

    @classmethod
    def getAll(cls):
        return dumps(cls.collection.find(),ensure_ascii=False).encode("utf8")

    @classmethod
    def getById(cls,id):
        return dumps(cls.collection.find_one({'_id' :ObjectId(id)}),ensure_ascii=False,indent=4, default=default).encode("utf8")
