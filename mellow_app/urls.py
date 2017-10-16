from django.conf.urls import url
from mellow_app import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^sign_up', views.sign_up),
    url(r'^request', views.sign_up_request),
]