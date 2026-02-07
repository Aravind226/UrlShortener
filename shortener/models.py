from django.db import models

class URL(models.Model):
    originalURL = models.URLField()
    shortenedURL = models.CharField(max_length=6, unique=True)
    visits = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
