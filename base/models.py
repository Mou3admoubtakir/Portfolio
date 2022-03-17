from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=300, blank=True, null=True)
    mini_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    date = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
