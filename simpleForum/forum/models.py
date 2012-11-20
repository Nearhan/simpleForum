from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Forum(models.Model):
	title = models.CharField(max_length=60)
	def __unicode__(self):
		return self.title


class Thread(models.Model):
	title = models.CharField(max_length=60)
	created = models.DateTimeField(auto_now_add=True)
	creater = models.ForeignKey(User, blank=True, null=True)
	forum = models.ForeignKey(Forum)

class Post(models.Model)
	title = models.CharField(max_length=60)
	created = models.DateField(auto_now_add=True)
	creater = models.ForeignKey(User, blank=True, null=True)
	thread = models.ForeignKey(Forum)
	body = models.CharField(max_length=10000)



