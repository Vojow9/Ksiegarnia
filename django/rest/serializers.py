from rest_framework import serializers
from sklep.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','author','title','description','tableOfContents','price','ebook','paper','graphics','published_date')
