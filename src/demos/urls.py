from django.conf.urls import include, url
from django.conf.urls import handler404
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import estadistica.urls
import maquetas.urls
from . import views

# Personalized admin site settings like title and header
admin.site.site_title = 'Demos Site Admin'
admin.site.site_header = 'Demos Administration'

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', admin.site.urls),
    url('', include(accounts.urls)),
    url(r'^estadistica/', include(estadistica.urls, namespace='estadistica')),
    url(r'^poc/', include(maquetas.urls)),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url('__debug__/', include(debug_toolbar.urls)),
    ]
