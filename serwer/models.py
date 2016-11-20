import json, pymongo
books_example = json.loads(open('examples.json','r').read())



class Books():

    def getAllBooks():
        return books_example


    def getAllIdAndTittles():
        return {b['id']:b['name'] for b in books_example}


    def getBookById(id):
        return next((b for b in books_example if b['id'] == id), None)

#print(Books.getAllTittles())
#print(Books.getBookById(1))

#print(Books.getAllTittles())
