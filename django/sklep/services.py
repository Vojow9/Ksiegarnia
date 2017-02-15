import requests
import os
import shutil




def getBooksList():
    books = requests.get('http://localhost:8080/books').json()
    return books

def getBookCoverById(id):
    url = id+'.jpg'
    des = r"C:\Users\Kasia\Desktop\Ksiegarnia-master\django\static\media\\"
    if os.path.isfile(des+url):
        return id
    else:
        cover = requests.get('http://localhost:8080/bookcovers/'+id)
        if cover == 0:
            return id
        else:
            im = open(des+url,'wb')
            im.write(cover.content)
            return url

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

def getCustomerById(id):
	customers = requests.get('http://localhost:8080/customers/' + id).json()
	return customers	
	
def getCustomersById(id):
	customers = requests.get('http://localhost:8080/customers/').json()
	return customers
	
def postBook(data):
    return requests.post('http://localhost:8080/books/',data)

if __name__ == '__main__':
    print(getBooksList())
