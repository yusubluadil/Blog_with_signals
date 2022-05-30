from .models import Blogs 
from author.models import AuthorPoint
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.v1.serializers import BlogSerializer, UserSerializer, AuthorPointSerializer


@receiver(post_save, sender = Blogs)
def new_point(sender, instance, created, **kwargs):
  if (created):
    author_point = AuthorPoint.objects.get(author = instance.author)
    author_point.point += 1
    author_point.save()