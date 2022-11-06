from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_data = models.DateTimeField(default=timezone.now)
    publisher_data = models.DateTimeField(blank=True, null=True)

    def publisher(self):
        self.publisher_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title
