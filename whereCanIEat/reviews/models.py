from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Restaurant(models.Model):
	def __str__(self):
		return "Name: " + self.name + ", City: " + self.city_name + ", Type: " + self.food_type
	name = models.CharField(max_length=30)
	city_name  = models.CharField(max_length=30)
	food_type = models.CharField(max_length=30)

class Review(models.Model):
	def __str__(self):
		return "Reviewer Name: " + self.reviewer_name + ", comment: " + self.comment + ", stars: " + str(self.stars)
	reviewer_name = models.CharField(max_length=30)
	comment = models.CharField(max_length=300)
	stars = models.IntegerField()
	name = models.CharField(max_length=20)
