from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.views import defaults as default_views
from home.urls import urlpatterns as home_urlpatterns


urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
    path('', include('pro_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + home_urlpatterns


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns

if 'imprint' in settings.INSTALLED_APPS:
    from imprint.views import AboutView
    urlpatterns += [
        url(r'^about/$', AboutView.as_view(), name='about'),
    ]
