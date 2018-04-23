from django.conf.urls import url
from landing import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^landing123/$', views.landing, name='landing'),
]