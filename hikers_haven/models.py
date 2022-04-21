from django.db import models

# Create your models here.

class Forum(models.Model):
    id = models.IntegerField(primary_key=True)
    topics = models.CharField(max_length=200, blank=False, null=False)
        
    def __str__(self):
        return self.topics