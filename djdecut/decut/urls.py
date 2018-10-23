from django.conf.urls import url
from django.contrib import admin
from .views import  dashboard,signup_view,feed_view
urlpatterns = [
    url(r'^$',dashboard),
    url(r'^signup',signup_view),
    url(r'^sucess',feed_view)
]
