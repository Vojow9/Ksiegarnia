from django.db import models
from django.utils import timezone

class Author(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	def add(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.name

class Book(models.Model):
	
	title = models.CharField(max_length=70)
	author =  models.ForeignKey(Author)
	ISBN = models.IntegerField()
	description = models.TextField()
	tableOfContents = models.TextField()
	price = models.IntegerField()
	ebook = models.BooleanField()
	graphics = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)
	def add(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title
		
	