from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<minute_changes_id>[0-9]+)/$', views.detail, name='detail'),
]
