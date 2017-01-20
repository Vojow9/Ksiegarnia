from models.model import Model
from models.authors import Authors
import json
from bson import ObjectId
from .DBItemIdParser import DBItemIdParser
from bson.json_util import dumps,default
from bson import Binary

class BookCovers(Model):
    collection = Model.db.bookcovers

    def getByIdOfBook(bookid,):
        print(type(bookid))
        print(bookid)
        collection = BookCovers.collection.find_one({'bookid' :ObjectId(bookid)})['image']
        print(type(collection))
        return collection


    def createByIdOfBook(bookid, bdata):
        from models.books import Books
        if type(Books.collection.find_one({'_id' :ObjectId(bookid)})) == type(None):
            return 400
        if type(BookCovers.collection.find_one({'bookid' :ObjectId(bookid)})) != type(None):
            return 409
        BookCovers.collection.insert_one({'bookid' :ObjectId(bookid) , 'image':Binary(bdata)})
        return 201

    #overrides
    def deleteById(bookid):
        BookCovers.collection.delete_one({'bookid' :ObjectId(bookid)})
