from .DBItemIdParser import DBItemIdParser
#from .DBItemIdParser import DBItemIdParser.prettyIdRepresentation
import json, pymongo
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps,default
from copy import deepcopy

class Model():

    def connect_to_database(host='localhost', port=27017):
        client = MongoClient(host, port)
        db = client.ksiegarniadb
        return db

    db = connect_to_database()

    @classmethod
    def getAll(cls):
        collection = list(cls.collection.find()) # cls.collection.find() needs to be converted form pymogno.cursor to list
        collection =DBItemIdParser.prettyIdRepresentation(collection)
        return dumps(collection,ensure_ascii=False).encode("utf8")


    @classmethod
    def getById(cls,id):
        collection = cls.collection.find_one({'_id' :ObjectId(id)})
        collection = DBItemIdParser.prettyIdRepresentation(collection)
        return dumps(collection,ensure_ascii=False,).encode("utf8")
