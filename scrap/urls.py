from django.conf.urls import url
from scrap import views


urlpatterns =[

    url(r'^search$', views.search),

]
