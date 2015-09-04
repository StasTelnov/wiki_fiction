from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexPapers.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.ShowPaper.as_view(), name='show'),
]
