from django.contrib import admin
from .models import AuthorPoint, CustomUser
from django.contrib.auth.models import Permission
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(AuthorPoint)
admin.site.register(Permission)
