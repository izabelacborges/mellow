from django.conf.urls import url
from mellow_app import views

urlpatterns = [
    url(r'^$', views.index),
]