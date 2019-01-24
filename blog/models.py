from django.conf import settings
#This will import settings from django.conf
from django.db import models

from django.utils import timezone

#This defines our model - Class is defining an object, Post is the name of our object, 
#models.Model tells Django that Post is a Django Model so it can be saved in the database
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
