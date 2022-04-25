from django.db import models

# Create your models here.
class Forum(models.Model):
    #name = models.CharField(max_length=200, blank=False, default='Discussion Topics')
    topics = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.topics

# one forum per topic but many topics per forum 
class Topic(models.Model):
    label = models.ForeignKey('Forum', on_delete=models.CASCADE, default=None)
    posts = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.label

# one topic and one user per post but many posts per topic and many posts per user
class Post(models.Model):
    title = models.ForeignKey('Topic', on_delete=models.CASCADE, default=None)
    content = models.CharField(max_length=5000, blank=False, null=False)
    date_added = models.DateField()
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)
    comments = models.CharField(max_length=900, blank=False, null=False)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    date_added = models.DateField()
    comm_by = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, default=None)
    comm_on = models.ForeignKey('Post', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.comm_by