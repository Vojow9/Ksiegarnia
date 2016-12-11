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


    #changes list of ObjectID type, to list of strings
    def prettyIdRepresentationOfItem(collection):
        try:
            collection['id']=str(collection['_id'])
            del collection['_id']
        except:
            pass
        for i in collection:
            if isinstance(collection[i],list) and isinstance(collection[i][0],ObjectId):
                collection[i] = [str(a) for a in collection[i]]
        return collection

    #changes "_id":{"$oid":" "5836049c57aac220c4c87384"} to simple $oid:" "5836049c57aac220c4c87384"
    def prettyIdRepresentation(collection):
        collection
        if  isinstance(collection,dict):
            return Model.prettyIdRepresentationOfItem(collection)
        return [Model.prettyIdRepresentationOfItem(item) for item in collection]

    @classmethod
    def getAll(cls):
        collection = list(cls.collection.find()) # tu mamy kursor
        collection = Model.prettyIdRepresentation(collection)
        return dumps(collection,ensure_ascii=False).encode("utf8")


    @classmethod
    def getById(cls,id):
        collection = cls.collection.find_one({'_id' :ObjectId(id)})
        collection = Model.prettyIdRepresentation(collection)
        return dumps(collection,ensure_ascii=False,indent=4, default=default).encode("utf8")

        #print(type(cls.collection.find_one({'_id' :ObjectId(id)})))
        #return dumps(cls.collection.find_one({'_id' :ObjectId(id)}),ensure_ascii=False,indent=4, default=default).encode("utf8")
