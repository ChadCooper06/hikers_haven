from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Forum, Topic, Post, Comment, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ('topics',)

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['label', 'posts']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['forum', 'title', 'content', 'date_added', 'pinned', 'user_id']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['date_added', 'comm_by', 'comm_on']