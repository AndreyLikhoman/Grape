from django.conf.urls import include, url
from django.contrib import admin
import os
from django.conf import settings
from django.conf.urls.static import static
PROJECT_DIR = os.path.dirname(__file__)

urlpatterns = [
    # Examples:
    # url(r'^$', 'grapeSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
