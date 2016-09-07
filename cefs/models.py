from django.db import models
from django.utils import timezone


class Chapter(models.Model):
	heading = models.CharField(max_length=200)
	date_completed = models.DateTimeField(blank=True, null=True)



	def __str__(self):
		return self.heading

class supChapter(models.Model):
	chapter = models.ForeignKey(Chapter)
	title = models.CharField(max_length=200)
	text = models.TextField()
	completedCourse = models.BooleanField(default=False)



	def __str__(self):
		return self.title