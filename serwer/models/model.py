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
    #and changes list of ObjectID type, to list of strings
    #maybe that should be recursive in some way?

    def prettyIdRepresentationOfItem(collection):
        prettyCollection = collection
        try:
            prettyCollection['id']=str(prettyCollection['_id'])
            del prettyCollection['_id']
        except:
            pass
        for i in prettyCollection:
            if isinstance(prettyCollection[i],list) and isinstance(prettyCollection[i][0],ObjectId):
                prettyCollection[i] = [str(a) for a in prettyCollection[i]]
        return prettyCollection


    def prettyIdRepresentation(collection):
        prettyCollection = collection
        print(type(collection))
        if  isinstance(prettyCollection,dict):
            return Model.prettyIdRepresentationOfItem(prettyCollection)
        return [Model.prettyIdRepresentationOfItem(item) for item in prettyCollection]

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
