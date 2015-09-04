from django.shortcuts import render
from django.views import generic
from .models import Paper


class IndexPapers(generic.ListView):
    template_name = 'papers/index.html'

    def get_queryset(self):
        return Paper.objects.all()[:10]


class ShowPaper(generic.DetailView):
    model = Paper
    template_name = 'papers/show.html'
