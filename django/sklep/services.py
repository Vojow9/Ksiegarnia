import requests


def getBooksList():
    books = requests.get('http://localhost:8080/books').json()
    print(books)
    return books
