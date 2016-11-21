from bottle import get, post
import models

@get('/books/all')
def booklist():
    return models.Books.getAllBooks()
    #print(models.Books.getAllBooks())
    #return str([1,2,3,4])
@get('/books/allIdAndTitles')
def booklist():
    return models.Books.getAllIdAndTittles()

@get('/books/<id>')
def booklist(id):
    return models.Books.getBookById(id)
