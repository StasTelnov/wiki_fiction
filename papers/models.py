from django.db import models
from django.contrib.auth.models import User
from .validators import between_validator


class Tag(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name


class Paper(models.Model):
    user = models.ForeignKey(User)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=30, db_index=True)
    text = models.TextField()
    rating = models.FloatField(null=False, default=0, validators=[between_validator(0, 10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User)
    paper = models.ForeignKey(Paper)
    text = models.TextField()
    rating = models.FloatField(validators=[between_validator(0, 10)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s..." % self.text[:10]
