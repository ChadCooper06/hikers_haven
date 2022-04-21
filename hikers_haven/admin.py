from django.contrib import admin
from .models import Forum, ForumTopic, Post

# Register your models here.
admin.site.register(Forum)
admin.site.register(ForumTopic)
admin.site.register(Post)