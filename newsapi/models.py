from django.db import models


class News(models.Model):
    author_name = models.CharField(max_length=50, default="SOME STRING")
    title = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=200, blank=True)
    vote = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"{self.id}, {self.author_name}, {self.title}"


class Comment(models.Model):
    content = models.ForeignKey(News, on_delete=models.CASCADE, related_name="comment")
    author_name = models.CharField(max_length=50, default="SOME STRING")
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name}, {self.created}"
