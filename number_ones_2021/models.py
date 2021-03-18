from django.db import models
from django.contrib.auth import get_user_model

class Hits(models.Model):
    title = models.CharField(max_length=32)
    album = models.CharField(max_length=32)
    description = models.TextField()
    artists = models.CharField(max_length=32)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


