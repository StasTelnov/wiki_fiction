from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name


class Paper(models.Model):
    user = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, related_name='papers')
    title = models.CharField(max_length=30, db_index=True)
    text = models.TextField()
    rating = models.FloatField(null=False, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('papers:show', args=[str(self.id)])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('papers:show', kwargs={'pk': self.pk})


class Comment(models.Model):
    user = models.ForeignKey(User)
    paper = models.ForeignKey(Paper)
    text = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s..." % self.text[:10]
