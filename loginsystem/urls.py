from django.conf.urls import url
from loginsystem import views


urlpatterns =[

    url(r'^signin$', views.signin),
    url(r'^signup$', views.signup),
    url(r'^signout$', views.signout),
    url(r'^results$', views.results),
    url(r'^contact$', views.contact),
    url(r'^about$', views.about),
    url(r'^$', views.home, name='home'),


]
