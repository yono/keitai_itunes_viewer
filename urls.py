from django.conf.urls.defaults import *
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^keitai/', include('keitai.itunes.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.+)$', 'django.views.static.serve',
        {'document_root':os.path.join(BASE_DIR,'templates')}),
)
