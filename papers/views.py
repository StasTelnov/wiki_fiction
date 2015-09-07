from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Paper


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class IndexPapers(LoginRequiredMixin, generic.ListView):
    template_name = 'papers/index.html'
    login_required = True

    def get_queryset(self):
        return Paper.objects.all()[:10]


class ShowPaper(LoginRequiredMixin, generic.DetailView):
    model = Paper
    template_name = 'papers/show.html'
