from django.conf.urls import url
from userdata import views


urlpatterns =[

    url(r'^create$', views.create),
    url(r'^mylyrics$', views.mylyrics),
    url(r'^delete$', views.delete),

]
