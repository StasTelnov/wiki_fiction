from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name


class Paper(models.Model):
    user = models.ForeignKey(User)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=30, db_index=True)
    text = models.TextField()
    rating = models.FloatField(null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User)
    paper = models.ForeignKey(Paper)
    text = models.TextField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s..." % self.text[:10]
