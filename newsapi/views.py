from rest_framework.generics import (
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
)
from newsapi.paginator import Paginator
from newsapi.serializers import NewsSerializer, CommentSerializer
from newsapi.models import News, Comment
from django.db.models import F


class NewsListView(ListAPIView):
    pagination_class = Paginator
    serializer_class = NewsSerializer


class NewsCreateView(CreateAPIView):
    serializer_class = NewsSerializer


class NewsUpdate(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = "id"


class CommentAddView(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"


class CommentDelView(RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"


class VoteView(UpdateAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    lookup_field = "id"

    def patch(self, request, *args, **kwargs):
        votes = News.objects.filter(id=kwargs["id"]).values("vote")
        votes.update(vote=F("vote") + 1)
        return self.partial_update(request, *args, **kwargs)
