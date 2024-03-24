from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings 
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


# sitemaps 
from django.contrib.sitemaps import views as sitemap_views
from exchange_rates.sitemaps import ExchangeRatesSitemap 

sitemaps = {
    'exchange_rates': ExchangeRatesSitemap,
}



# for rest api 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi





schema_view = get_schema_view(
   openapi.Info(
      title="Educify api",
      default_version='v1',
      description="Educify api documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("adminsitepanal/", admin.site.urls),
    path("", include("exchange_rates.urls")),

    prefix_default_language=False,




) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

from django.utils.translation import gettext_lazy as _
