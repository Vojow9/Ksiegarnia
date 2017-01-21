from models.model import Model
from models.authors import Authors
from models.bookcovers import BookCovers
import json
from bson import ObjectId


class Books(Model):
    collection = Model.db.books

    def isValidBookForm(book):
        try:
            book = json.loads(str(book,'utf8'))
            for o in ('ISBN','title','isEbook','price','availability',
            'authors','tableOfContents','description'):
                if o not in book:
                    assert False
            if type(book['isEbook']) != type(True):
                assert False
            if type(book['tableOfContents']) != list:
                assert False
            for author in book['authors']:
                if type(Authors.getById(author,strFormat = True)) == type(None):
                    assert False
            return True
        except:
            return False


    def isAuthorInAnyBook(author):
        authorsList = []
        for book in list(Books.collection.find()):
            authorsList.extend(book['authors'])
        return ObjectId(author) in authorsList


    def deleteById(id):
        if not Books.isValueUsed('_id',ObjectId(id)):
            return 404
        BookCovers.deleteById(id)
        Books.collection.delete_one({'_id' :ObjectId(id)})
        return 200

    def changeAuthorStrIdToObjectId(authorslist):
        new_list = list()
        for a in authorslist:
            new_list.append(ObjectId(a))
        return new_list

    def createBook(new_book):
        if not Books.isValidBookForm(new_book):
            return 400
        new_book = json.loads(str(new_book,'utf8'))
        new_book['authors'] = Books.changeAuthorStrIdToObjectId(new_book['authors'])
        if Books.isValueUsed("ISBN",new_book["ISBN"]):
            return 409
        Books.collection.insert_one(new_book)
        return 201

    def isBooksIdsValidId(bookslist):
        bookslist = [ObjectId(bookid) for bookid in bookslist]
        print(bookslist)
        for b in bookslist:
            if type(Books.collection.find_one({'_id':b})) == type(None):
                return False
        return True


    def isBooksAvailable(bookslist):
        bookslist = [ObjectId(bookid) for bookid in bookslist]
        for b in bookslist:
            quantity = bookslist.count(b)
            if Books.collection.find_one({'_id':b})['isEbook'] == False and \
             Books.collection.find_one({'_id':b})['availability'] < quantity:
                return False
        return True


    def isMoreThanOneEbook(bookslist):
        bookslist = [ObjectId(bookid) for bookid in bookslist]
        for b in bookslist:
            quantity = bookslist.count(b)
            if Books.collection.find_one({'_id':b})['isEbook'] == True and quantity >= 2:
                return True
        return False


    def decreaseAvailability(bookslist):
        bookslist = [ObjectId(bookid) for bookid in bookslist]
        digested = []
        for b in bookslist:
            if b in digested:
                break
            else:
                digested.append(b)
            quantityOfBuyed = bookslist.count(b)
            quantityInDb = Books.collection.find_one({'_id':b})['availability']
            if Books.collection.find_one({'_id':b})['isEbook'] == False:
                Books.collection.update_one({'_id':b}, {'$set': {'availability': quantityInDb - quantityOfBuyed}})


    def isEbook(id):
        return Books.collection.find_one({'_id':ObjectId(id)})['isEbook']
