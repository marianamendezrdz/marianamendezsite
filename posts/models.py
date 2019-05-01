from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title #makes it so that list of blog posts in django admin are entitled as the title written
    class Meta:
        verbose_name_plural = "Posts" #makes it so that new model in django admin is not plural

#make sure to migrate new models!!!!!
#make sure to migrate new models!!!!!
#make sure to migrate new models!!!!!

# create database file: --> python manage.py makemigrations [replace with model name]
# create database table: --> python manage.py migrate
