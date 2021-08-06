from django.db import models
from django.utils import timezone

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    write_date = models.DateTimeField(timezone.localtime())
    modify_date = models.DateTimeField(timezone.localtime())

    def __str__(self):
        return self.title

    def shortcut(self):
        return self.body[:50]
