from .models import CustomUser, AuthorPoint
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender = CustomUser)     # post_save CustomUser modeli create oldugu zaman bu prosesi yerine yetir demekdir
def create_author_point(sender, instance, created, **kwargs):
  # created booldur ya True ya da False olur, instance CustomUser-in obyektidir.
  if (created):
    AuthorPoint.objects.create(author = instance)

# author.apps-in icine bax
