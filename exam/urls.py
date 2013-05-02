from django.conf.urls import patterns, include, url

from exam import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^details/', views.details, name='details'),
    url(r'^(?P<ques_id>\d+)/check/$', views.check, name='check'),
)