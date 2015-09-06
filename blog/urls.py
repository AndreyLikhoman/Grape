from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^post/(?P<url>[\w -]+)/$', views.post_detail, name='post_detail'),
    url(r'^category/(?P<url>[\w -]+)/$', views.category_detail, name='category_detail'),
]