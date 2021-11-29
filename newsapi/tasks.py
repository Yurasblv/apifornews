from celery import shared_task
from newsapi.models import News


@shared_task
def clear_data():
    for post in News.objects.all():
        post.vote = 0
        post.save()
