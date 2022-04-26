from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Forum, Topic, Post, Comment

class CustomUserAdmin(UserAdmin):    
    model = CustomUser
    list_display = ['email']

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comment)

