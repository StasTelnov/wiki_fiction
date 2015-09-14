from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.show, name='show'),
    url(r'^new/$', views.new, name='new'),
    # url(r'^create/$', views.create, name='create'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit, name='edit'),
    # url(r'^(?P<pk>[0-9]+)/update/$', views.update, name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.delete, name='delete'),
]

# urlpatterns = [
#     url(r'^$', views.IndexPapers.as_view(), name='index'),
#     url(r'^(?P<pk>[0-9]+)/$', views.ShowPaper.as_view(), name='show'),
#     url(r'^new/$', views.NewPaper.as_view(), name='new'),
#     # url(r'^create/$', views.ShowPaper.as_view(), name='create'),
# ]
