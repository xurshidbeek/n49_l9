from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # id = models.BigIntegerField(
    #     primary_key=True, unique=True, editable=False, default=uuid4)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner} - {self.title}"
