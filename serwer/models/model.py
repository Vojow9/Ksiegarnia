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
    def prettyIdRepresentation(collection):
        prettyCollection = collection
        print(type(collection))
        if  isinstance(prettyCollection,dict):
            try:
                prettyCollection['id']=str(prettyCollection['_id'])
                del prettyCollection['_id']
            except:
                pass
            for i in prettyCollection:
                if isinstance(prettyCollection[i],list) and isinstance(prettyCollection[i][0],ObjectId):
                    prettyCollection[i] = [str(a) for a in prettyCollection[i]]
            return prettyCollection


        for item in prettyCollection:
            try:
                item['id']=str(item['_id'])
                del item['_id']
            except:
                pass
            for i in item:
                if isinstance(item[i],list) and isinstance(item[i][0],ObjectId):
                    item[i] = [str(a) for a in item[i]]
        return prettyCollection

    @classmethod
    def getAll(cls):
        collection = list(cls.collection.find()) # tu mamy kursor
        collection = Model.prettyIdRepresentation(collection)
        return dumps(collection,ensure_ascii=False).encode("utf8")


    @classmethod
    def getById(cls,id):
        print(type(cls.collection.find_one({'_id' :ObjectId(id)})))
        print('='*30)
        print(cls.collection.find_one({'_id' :ObjectId(id)}))
        print('='*30)
        collection = cls.collection.find_one({'_id' :ObjectId(id)})
        collection = Model.prettyIdRepresentation(collection)
        return dumps(collection,ensure_ascii=False,indent=4, default=default).encode("utf8")

        #print(type(cls.collection.find_one({'_id' :ObjectId(id)})))
        #return dumps(cls.collection.find_one({'_id' :ObjectId(id)}),ensure_ascii=False,indent=4, default=default).encode("utf8")
