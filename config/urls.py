from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from apps.core.views import robots_txt


sitemaps = {

}


urlpatterns = [

    path('admin/', admin.site.urls),

    path('robots.txt', robots_txt),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),

    path('', TemplateView.as_view(template_name='index.html'), name='home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns = [

        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns