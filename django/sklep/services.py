import requests


def getBooksList():
    books = requests.get('http://localhost:8080/books').json()
    print(books)
    return books


def getBookById(id):
    books = requests.get('http://localhost:8080/books/' + id).json()
    print(books)
    return books
