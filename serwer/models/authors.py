from models.model import Model
import json
from bson import ObjectId

import models.books

class Authors(Model):
    collection = Model.db.authors

    def isValidAuthorForm(author):
        try:
            author = json.loads(str(author,'utf8'))
            if not 'description' in author and not 'name' in author:
                assert False
            if len(author) > 2:
                assert False
            if not Model.properLenOfObject(author["name"]):
                assert False
            return True
        except:
                return False

    def nameIsUsed(username):
        if Authors.collection.find_one({'name':username}) is not None:
            return True
        else:
            return False

    #overrides
    def deleteById(id):

        if models.books.Books.isAuthorInAnyBook(id):
            return 403
        if not Authors.isValueUsed('_id',ObjectId(id)):
            return 404
        Authors.collection.delete_one({'_id' :ObjectId(id)})
        return 200

    def createAuthor(new_author):
        if not Authors.isValidAuthorForm(new_author):
            return 400
        new_author = json.loads(str(new_author,'utf8'))
        if Authors.isValueUsed("name",new_author['name']):
            return 409
        result = Authors.collection.insert_one(new_author)
        return 201
