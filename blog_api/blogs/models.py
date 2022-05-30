from django.db import models
from django.contrib.auth.models import User
from author.models import CustomUser
# Create your models here.

class Blogs(models.Model):
  title = models.CharField(max_length = 150)
  content = models.TextField()
  author = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = "blogs")
  created  = models.DateField(auto_now_add = True)
  
  def __str__(self):
    return self.title