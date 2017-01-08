import requests


def getBooksList():
    books = requests.get('http://localhost:8080/books').json()
    return books


def getBookById(id):
    books = requests.get('http://localhost:8080/books/' + id).json()
    return books

def getBook():
	books = requests.get('http://localhost:8080/books').json()
	return books

def getAuthorsList():
    authors = requests.get('http://localhost:8080/authors').json()
    return authors


def getAuthorById(id):
    authors = requests.get('http://localhost:8080/authors/' + id).json()
    return authors

def postBook(data):
    return requests.post('http://localhost:8080/books/',data)

if __name__ == '__main__':
    print(getBooksList())
