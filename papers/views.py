# from django.contrib.auth.decorators import permission_required
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Paper, Comment
from .forms import PaperForm, CommentForm


def index(request):
    papers = Paper.objects.all().select_related(
        'user').prefetch_related('tags').order_by('id')

    paginator = Paginator(papers, 10)
    page = request.GET.get('page')
    try:
        papers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        papers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        papers = paginator.page(paginator.num_pages)

    return render(request, 'papers/index.html',
                  {'paper_list': papers})


def show(request, paper_id):
    try:
        paper = Paper.objects.prefetch_related(
            'comments__user').get(pk=paper_id)
    except Paper.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.paper = paper
            comment.save()
            messages.success(request, 'Comment was successfully added')
            return redirect(paper)
    else:
        comment_form = CommentForm()

    return render(request, 'papers/show.html',
                  {'paper': paper, 'comment_form': comment_form})


# @permission_required('papers.delete_comment')
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment was successfully deleted')
    return redirect(comment.paper)


# @permission_required('papers.add_paper')
def new(request):
    if request.method == 'POST':
        form = PaperForm(request.POST)
        if form.is_valid():
            paper = form.save(commit=False)
            paper.user = request.user
            paper.save()
            form.save_m2m()

            messages.success(request, 'Paper was successfully created')
            return redirect(paper)
    else:
        form = PaperForm()

    return render(request, 'papers/new.html', {'form': form})


# @permission_required('papers.change_paper')
def edit(request, paper_id):
    paper = get_object_or_404(Paper, pk=paper_id)
    form = PaperForm(request.POST or None, instance=paper)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Paper was successfully updated')
        return redirect(paper)

    return render(request, 'papers/edit.html', {'form': form})


# @permission_required('papers.delete_paper')
def delete(request, paper_id):
    paper = get_object_or_404(Paper, pk=paper_id)
    paper.delete()
    messages.success(request, 'Paper was successfully deleted')

    return redirect(reverse('papers:index'))
