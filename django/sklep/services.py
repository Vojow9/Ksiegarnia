import requests


def getBooksList():
    books = requests.get('http://localhost:8080/books').json()
    return books


def getBookById(id):
    books = requests.get('http://localhost:8080/books/' + id).json()
    return books


if __name__ == '__main__':
    print(getBooksList())
