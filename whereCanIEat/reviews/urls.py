from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'add/', views.add, name='add'),
    url(r'^(?P<city>[a-z,A-Z]+)/$', views.city, name='city'),
]
