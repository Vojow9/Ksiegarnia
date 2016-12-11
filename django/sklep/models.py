from django.db import models
from django.utils import timezone


class Book(models.Model):
	author = models.CharField(max_length=50)
	title = models.CharField(max_length=70)
	description = models.TextField()
	tableOfContents = models.TextField()
	price = models.IntegerField()
	ebook = models.CharField(max_length=30)
	paper = models.CharField(max_length=30)
	graphics = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)

	def add(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title
