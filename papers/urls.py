from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<paper_id>[0-9]+)/$', views.show, name='show'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<paper_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<paper_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<comment_id>[0-9]+)/comment/delete$', views.delete_comment,
        name='delete_comment'),
]
