from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prueba.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^' , include('apps.tienda.urls')),
    url(r'', include('getpaid.urls')),
    url(r'^media/(?P<path>.*)$' , 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),

)
