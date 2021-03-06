from django.conf.urls import *
from plot import views

urlpatterns = patterns('django.views.generic.simple',

    url(r'^$', views.index, name='plots'),
    url(r'^find', views.index, name='find'),
    url(r'^preview', views.preview, name='preview'),
    url(r'^plot', views.plot, name='plot'),
    url(r'^save', views.save, name='save'),
    url(r'^update', views.update, name='update'),
 )
