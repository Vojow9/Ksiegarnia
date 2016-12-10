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

    #changes "_id":{"$oid":" "5836049c57aac220c4c87384"} to simple $oid:" "5836049c57aac220c4c87384"
    #maybe that should be recursive in some way?
    def prettyIdRepresentation(collection):
        prettyCollection = list(collection.find())
        for item in prettyCollection:
            item['$oid']=str(item['_id'])
            del item['_id']
        print(prettyCollection)
        return prettyCollection

    @classmethod
    def getAll(cls):
        collection = Model.prettyIdRepresentation(cls.collection)
        #print(dumps(cls.collection.find(),ensure_ascii=False).encode("utf8"))
        return dumps(collection,ensure_ascii=False).encode("utf8")




    @classmethod
    def getById(cls,id):
        return dumps(cls.collection.find_one({'_id' :ObjectId(id)}),ensure_ascii=False,indent=4, default=default).encode("utf8")
