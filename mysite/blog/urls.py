from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.post_list, name='post_list'),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<poll_id>\\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<polls>\\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\\d+)/vote/$', views.vote, name='vote'),
)
