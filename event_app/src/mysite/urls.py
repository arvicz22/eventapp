from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'event_share.views.home', name='home'),
    url(r'^create/$', 'event_share.views.create', name='create'),
    # url(r'events^$', 'event_share.views.home', name='showevents'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,	
							document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,
							document_root=settings.MEDIA_ROOT)