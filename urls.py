from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from crawler.views import *
from searchengine.views import *
from mainapp.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackingpot.views.home', name='home'),
    # url(r'^hackingpot/', include('hackingpot.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
#	url(r'^search/', search.views.search),
	url(r'^crawl', crawl),
	url(r'^$', main),
	url(r'^search', search),
	url(r'^about', about),
)
