from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^details/(?P<id>\d+)', views.detail, name="details"),
    url(r'^add/$', views.add, name="add")
]



