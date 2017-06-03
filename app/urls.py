from django.conf.urls import url

from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^policies/$', views.policies, name='policies'),
    url(r'^refer/$', views.refer, name='refer'),
    url(r'^schedule/$', views.schedule, name='schedule'),
    url(r'^volunteer/$', views.volunteer, name='volunteer'), 
    url(r'^BookNow/$', views.BookNow, name='BookNow'), 
]