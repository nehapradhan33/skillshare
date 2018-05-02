from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
     url(r'^$', 'signups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
