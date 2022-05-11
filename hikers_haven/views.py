from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import CustomUser
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CustomUserSerializer, ForumSerializer, TopicSerializer, PostSerializer, CommentSerializer

from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth.models import User
from hikers_haven.models import Forum, Topic, Post, Comment, CustomUser



class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# Create your views here.

class ForumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the forums to be viewed or edited
    """
    queryset = Forum.objects.all().order_by('-topics')
    serializer_class = ForumSerializer
    #permission_classes = [permissions.IsAuthenticated]

class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the topics to be viewed or edited.
    """
    queryset = Topic.objects.all().order_by('-label')
    serializer_class = TopicSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all the posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['forum_id'] # Filters the posts by forum they are on
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('-date_added')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]