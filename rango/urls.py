from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_user_details/$', views.add_user_details, name='add_user_details'),)

