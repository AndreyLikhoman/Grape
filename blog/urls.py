from django.conf.urls import include, url
from . import views, registration

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^personal/$',  registration.login , name="login"),
    url(r'^personal/(?P<id>[\w -]+)/$', registration.is_true, name='is_true'),
    url(r'/fff/^$', registration.is_false, name='is_false'),
    url(r'^galereya/$', views.return_galeries, name='return_galeries'),
    url(r'^galereya/(?P<url>[\w -]+)/$', views.galery_detail, name='galery_detail'),
    url(r'^media/$', views.return_medias, name='return_medias'),
    url(r'^media/(?P<url>[\w -]+)/$', views.return_videos, name='return_videos'),
    url(r'^accounts/logout/$', registration.logout),
    url(r'^(?P<category>[\w -]+)/(?P<url>[\w -]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<url>[\w -]+)/$', views.category_detail, name='category_detail'),
    
]