from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=200)
	url = models.URLField()
	image = models.URLField()
	parts = models.ManyToManyField('Part')
	
	def __str__(self):
		return self.name

class Part(models.Model):
	name = models.CharField(max_length=80)
	
	def __str__(self):
		return self.name
