from django.db import models

class Post(models.Model):
	content=models.TextField()
	title=models.CharField(max_length=250)


	def __str__(self):
		return self.title