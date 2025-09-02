# TODO There's certainly more than one way to do this task, so take your pick.

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets

class PostPagination(PageNumberPagination):
    page_size = 10  # how many posts per page 
    page_size_query_param = "page_size"
    max_page_size = 50



class PostListView(generics.ListAPIView):
    """
    API endpoint: List of Posts with latest 3 Comments each.

    URL: /api/posts/

    Query Params:
        - page (int): page number, e.g. /api/posts/?page=2
        - page_size (int, optional): override default (10), e.g. /api/posts/?page=2&page_size=20

    Response:
    {
        "count": 25,
        "next": "http://localhost:8000/api/posts/?page=2",
        "previous": null,
        "results": [
            {
                "id": 1,
                "text": "Sample post text",
                "timestamp": "2025-09-01T10:00:00Z",
                "author": "Rishee",
                "comment_count": 5,
                "comments": [
                    {
                        "id": 11,
                        "text": "Nice post!",
                        "timestamp": "2025-09-01T10:05:00Z",
                        "author": "CharecterHub"
                    },
                    ...
                ]
            }
        ]
    }

    Follow-up Answer:
        If you want 3 RANDOM comments instead of latest 3, change:

            obj.comments.order_by("-timestamp")[:3]

        to:

            obj.comments.order_by("?")[:3]
    """

    serializer_class = PostSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        return Post.objects.all().order_by("-timestamp").prefetch_related("comments", "author")

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    