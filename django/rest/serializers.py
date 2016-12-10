from django.contrib.auth.models import User
from rest_framework import serializers
from sklep.models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','author','title','description','tableOfContents','price','graphics','published_date')

class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'books')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')
    # id = serializers.IntegerFields(readonly=True)
    # author = serializers.CharField(required=False, allow_blank=True, max_lenght=50)
    # title =serializers.CharField(required=True, allow_blank=False, max_lenght=70)
    # description = serializers.TextField(required=False, allow_blank=True)
    # tableOfContents = serializers.TextField(required=False, allow_blank=True)
    # price = serializers.IntegerField(required=True, allow_blank=False)
    # graphics = serializers.TextField(required=False, allow_blank=True)
    # published_date = serializers.DataTimeField(allow_blank= True)
    #
    # def create(self, validated_data):
    #
    #     return Book.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #
    #     instance.author = validated_data.get('author', instance.title)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.title)
    #     instance.tableOfContents = validated_data.get('tableOfContents', instance.title)
    #     instance.price = validated_data.get('price', instance.title)
    #     instance.graphics = validated_data.get('graphics', instance.title)
    #     instance.published_date = validated_data.get('published_date', instance.title)
    #     instance.save()
    #     return instance