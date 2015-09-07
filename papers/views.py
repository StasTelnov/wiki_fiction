from django.contrib.auth.decorators import login_required
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


@login_required()
def welcome(request):
    return render(request, 'papers/welcome.html')

