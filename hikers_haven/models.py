from django.db import models

# Create your models here.
class Forum(models.Model):
    topics = models.ForeignKey('ForumTopic', on_delete=models.CASCADE)

    def __str__(self):
        return self.topics

# one forum per topic but many topics per forum 
class ForumTopic(models.Model):
    label = models.CharField(max_length=200, blank=False, null=False)
    posts = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.label

# one topic and one user per post but many posts per topic and many posts per user
class Post(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    content = models.CharField(max_length=5000, blank=False, null=False)
    date_added = models.DateField()
    user_id = models.ForeignKey('auth.User', on_delete=DO_NOTHING)
    comment = models.ForeignKey('Comment', on_delete=CASCADE)

    def __str__(self):
        return self.title

# one address and one anniversary per person but many people per anniversary and address
'''
class Person(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    anniversary = models.ForeignKey(
        'app_label.Anniversary', on_delete=models.CASCADE)
    address = models.ForeignKey(
        'app_label.Address', on_delete=models.CASCADE)

class Address(models.Model):
    line1 = models.CharField(max_length=150)
    line2 = models.CharField(max_length=150)
    postalcode = models.CharField(max_length=10)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

class Anniversary(models.Model):
    date = models.DateField()
    '''