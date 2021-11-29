from django.urls import path
from newsapi.views import (
    NewsListView,
    NewsCreateView,
    NewsUpdate,
    CommentAddView,
    CommentDelView,
    VoteView,
)


app_name = "myapp"


urlpatterns = [
    path("", NewsListView.as_view()),
    path("create/", NewsCreateView.as_view()),
    path("update/<int:id>", NewsUpdate.as_view()),
    path("comment/add/<int:id>", CommentAddView.as_view()),
    path("comment/delete/<int:id>", CommentDelView.as_view()),
    path("vote/<int:id>", VoteView.as_view()),
]
