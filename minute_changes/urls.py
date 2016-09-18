from django.conf.urls import url
from . import views

app_name = 'minute_changes'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<minute_changes_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^practise/(?P<chord_pair_id>[0-9]+)/$', views.PractiseView.as_view(), name='practise'),
]
