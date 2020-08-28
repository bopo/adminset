from django.conf.urls import include, url
from django.contrib import admin

from service.cmdb import asset
from .views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^cmdb/', include('service.cmdb.urls')),
    url(r'^navi/', include('service.navi.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^setup/', include('service.setup.urls')),
    url(r'^monitor/', include('service.monitor.urls')),
    url(r'^config/', include('service.configure.urls')),
    url(r'^accounts/', include('service.accounts.urls')),
    url(r'^appconf/', include('service.appconf.urls')),
    url(r'^delivery/', include('service.delivery.urls')),
    url(r'^mfile/', include('mfile.urls')),
    url(r'^elfinder/', include('service.elfinder.urls')),
    url(r'^branches/', include('service.branches.urls')),
    url(r'^webssh/(?P<ids>\d+)/$', asset.webssh, name='webssh'),

]
