from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import FormView
from .models import Paper
from .forms import PaperForm


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class IndexPapers(LoginRequiredMixin, generic.ListView):
    template_name = 'papers/index.html'

    def get_queryset(self):
        return Paper.objects.all()[:10]


class ShowPaper(LoginRequiredMixin, generic.DetailView):
    model = Paper
    template_name = 'papers/show.html'


class NewPaper(LoginRequiredMixin, FormView):
    template_name = 'papers/new.html'
    form_class = PaperForm
    success_url = 'papers/show'

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super(NewPaper, self).form_valid(form)
