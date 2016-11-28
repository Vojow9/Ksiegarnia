from models.model import Model

class Books(Model):
    collection = Model.db.books

    def getAuthors(id):
        return dumps(Books.collection.find())
