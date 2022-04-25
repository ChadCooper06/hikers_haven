from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from hikers_haven.models import Forum, Topic, Post, Comment
from rest_framework import viewsets
from rest_framework import permissions
from hikers_haven.serializers import UserSerializer, ForumSerializer, TopicSerializer, PostSerializer, CommentSerializer

def index(request):
    return HttpResponse('We\'re going to do what we do every night Pinky...try to take over the world!' 
        '\n NARF!')

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ForumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the forums to be viewed or edited
    """
    queryset = Forum.objects.all().order_by('topics')
    serializer_class = ForumSerializer
    permission_classes = [permissions.IsAuthenticated]

class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the topics to be viewed or edited.
    """
    queryset = Topic.objects.all().order_by('label')
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all the posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-date_added')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('-date_added')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]