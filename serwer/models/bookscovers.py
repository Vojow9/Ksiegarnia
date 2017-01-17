from models.model import Model
from models.authors import Authors
import json
from bson import ObjectId
from .DBItemIdParser import DBItemIdParser
from bson.json_util import dumps,default

class BookCovers(Model):
    collection = Model.db.bookcovers

    def getByIdOfBook(bookid,):
        collection = BookCovers.collection.find_one({'bookid' :ObjectId(bookid)})['image']
        return collection

    # def isValidUserForm(book):
    #     try:
    #         book = json.loads(str(book,'utf8'))
    #         for o in ('ISBN','title','isEbook','lendPrice','price','availability',
    #         'authors','cover','tableOfContents','description'):
    #             if o not in book:
    #                 assert False
    #         if type(book['isEbook']) != type(True):
    #             assert False
    #         if not type(book['isEbook']) in (type(True), type(None)):
    #             assert False
    #         if type(book['tableOfContents']) != list:
    #             assert False
    #         if book['isEbook'] == True and book['lendPrice'] is None:
    #             assert False
    #         if book['isEbook'] == False and book['lendPrice'] is not None:
    #             assert False
    #         for author in book['authors']:
    #             if type(Authors.getById(author,strFormat = True)) == type(None):
    #                 assert False
    #         return True
    #     except:
    #             return False

    #
    # def createBook(new_book):
    #     if not Books.isValidUserForm(new_book):
    #         return 400
    #     new_book = json.loads(str(new_book,'utf8'))
    #     if Books.isValueUsed("ISBN",new_book["ISBN"]):
    #         return 409
    #     Books.collection.insert_one(new_book)
    #     return 201
