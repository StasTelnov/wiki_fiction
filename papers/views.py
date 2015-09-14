# from django.contrib.auth.decorators import login_required
# from django.views import generic
# from django.views.generic.edit import FormView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Paper
from .forms import PaperForm
from django.contrib import messages
from django.core.urlresolvers import reverse


def index(request):
    papers = Paper.objects.all().order_by('id')
    for paper in papers:
        for tag in paper.tags.all():
            paper.tag_names = tag.name

    return render(request, 'papers/index.html', {'paper_list': papers})


def show(request, pk):
    instance = get_object_or_404(Paper, pk=pk)

    return render(request, 'papers/show.html', {'paper': instance})


def new(request):
    if request.method == 'POST':
        form = PaperForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save_m2m()

            messages.success(request, 'Paper was successfully created')
            return redirect(instance)
    else:
        form = PaperForm()

    return render(request, 'papers/new.html', {'form': form})


def edit(request, pk):
    instance = get_object_or_404(Paper, pk=pk)
    form = PaperForm(request.POST or None, instance=instance)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Paper was successfully updated')
        return redirect(instance)

    return render(request, 'papers/edit.html', {'form': form})


def delete(request, pk):
    instance = get_object_or_404(Paper, pk=pk)
    instance.delete()

    return redirect(reverse('papers:index'))

# class LoginRequiredMixin(object):
#     @classmethod
#     def as_view(cls, **initkwargs):
#         view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
#         return login_required(view)
#
#
# class IndexPapers(LoginRequiredMixin, generic.ListView):
#     template_name = 'papers/index.html'
#
#     def get_queryset(self):
#         return Paper.objects.all()[:10]
#
#
# class ShowPaper(LoginRequiredMixin, generic.DetailView):
#     model = Paper
#     template_name = 'papers/show.html'
#
#
# class NewPaper(LoginRequiredMixin, FormView):
#     template_name = 'papers/new.html'
#     form_class = PaperForm
#     success_url = 'papers/show'