from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

# Create your models here.
class Forum(models.Model):
    topics = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.topics

# one forum per topic but many topics per forum 
class Topic(models.Model):
    f_name = models.ForeignKey('Forum', on_delete=models.CASCADE, default=None)
    label = models.CharField(max_length=100, blank=False, null=False)
    posts = models.ForeignKey('Post', on_delete=models.PROTECT)

    def __str__(self):
        return self.label

# one topic and one user per post but many posts per topic and many posts per user
class Post(models.Model):
    forum = models.ForeignKey('Forum', on_delete=models.PROTECT, default=2)
    title = models.CharField(max_length=200, blank=False, default='New Post')
    content = models.CharField(max_length=5000, blank=False, null=False)
    date_added = models.DateField()
    user_id = models.ForeignKey('CustomUser', on_delete=models.PROTECT)
    #comments = models.CharField(max_length=2000, blank=False, default=None)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title
        #return f"{self.title} {self.content}"

class Comment(models.Model):
    date_added = models.DateField()
    content = models.CharField(max_length=2000, blank=False, default=None)
    comm_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    comm_on = models.ForeignKey('Post', default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.content