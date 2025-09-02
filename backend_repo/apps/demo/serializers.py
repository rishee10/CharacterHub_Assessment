# TODO There's certainly more than one way to do this task, so take your pick.

from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "timestamp", "author"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    comment_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "text", "timestamp", "author", "comment_count", "comments"]

    def get_comment_count(self, obj):
        return obj.comments.count()

    def get_comments(self, obj):
        # Fetch latest 3 comments
        qs = obj.comments.order_by("-timestamp")[:3]
        return CommentSerializer(qs, many=True).data

