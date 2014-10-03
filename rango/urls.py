from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_user_details/$', views.add_user_details, name='add_user_details'),
    url(r'^show_user_details/$', views.show_user_details, name='show_user_details'),
    url(r'^(?P<user_name_url>\w+)/cash_flow_proj_plan/$', views.cash_flow_proj_plan, name='cash_flow_proj_plan'),
    url(r'^(?P<user_name_url>\w+)/retirement_plan/$', views.retirement_plan, name='retirement_plan'),
    url(r'^(?P<user_name_url>\w+)/insurance_plan/$', views.insurance_plan, name='insurance_plan'),)

