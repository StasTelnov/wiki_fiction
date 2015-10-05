from django.db.models.signals import post_save
from django.dispatch import receiver
from papers.models import Comment, Paper
from django.db.models import Avg


@receiver(post_save, sender=Comment, dispatch_uid='recalculate_paper_rating')
def recalculate_paper_rating(sender, instance, **kwargs):
    rating = instance.paper.comments.aggregate(Avg('rating'))['rating__avg']
    Paper.objects.filter(id=instance.paper.id).update(rating=rating)
