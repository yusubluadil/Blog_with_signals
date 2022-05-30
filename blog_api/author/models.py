from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
  def __str__(self):
    return self.username

class AuthorPoint(models.Model):
  author = models.OneToOneField(CustomUser, related_name = "author_points", on_delete = models.CASCADE)
  point = models.PositiveIntegerField(default = 0)
  
  def __str__(self) -> str:
    return f"{self.author} - {self.point}"