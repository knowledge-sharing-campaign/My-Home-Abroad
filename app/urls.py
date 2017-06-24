from django.conf.urls import url

from . import views

from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^policies/$', views.policies, name='policies'),
    url(r'^home/$', views.home, name='home'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^volunteer_profile/$', views.profile, name='volunteer_profile'),
    url(r'^refer/$', views.refer, name='refer'),
    url(r'^schedule/$', views.schedule, name='schedule'),
    url(r'^volunteer/$', views.volunteer, name='volunteer'),
    url(r'^bookNow/$', views.bookNow, name='bookNow'),
    url(r'^register/$', views.register, name='register'),
    url(r'^traveller_reg/$', views.traveller_reg, name='traveller_reg'),
     url(r'^about/$', views.about, name='about'),
     url(r'^forgetting_passwd/$', views.forgetting_passwd, name='forgetting_passwd'),
     url(r'^my_schedul/$', views.my_schedul, name='my_schedul'),
]
