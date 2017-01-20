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
    def getById(cls,id,strFormat = False):
        collection = cls.collection.find_one({'_id' :ObjectId(id)})
        collection = DBItemIdParser.prettyIdRepresentation(collection)
        if strFormat == False:
            return dumps(collection,ensure_ascii=False,).encode("utf8")
        else:
            return collection

    @classmethod
    def deleteById(cls, id):
        cls.collection.delete_one({'_id' :ObjectId(id)})


    @classmethod
    def isValueUsed(cls,key,value):
        if cls.collection.find_one({key:value}) is not None:
            return True
        else:
            return False

    def properLenOfObject(obj, max_len = 30):
        if not ( 0 < len(obj) < max_len ):
            return False
        else:
            return True
