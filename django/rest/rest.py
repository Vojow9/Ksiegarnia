import coreapi

client = coreapi.Client()

schema = client.get('http://127.0.0.1:8000/schema/')

books = client.action(schema,'books')