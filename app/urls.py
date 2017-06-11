from django.conf.urls import url

from . import views

from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index'), 
<<<<<<< HEAD
=======
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
>>>>>>> 779635470fd01d924b127fef729b8836e0e42711
    url(r'^policies/$', views.policies, name='policies'),
    url(r'^refer/$', views.refer, name='refer'),
    url(r'^schedule/$', views.schedule, name='schedule'),
    url(r'^volunteer/$', views.volunteer, name='volunteer'), 
    url(r'^BookNow/$', views.BookNow, name='BookNow'), 
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]