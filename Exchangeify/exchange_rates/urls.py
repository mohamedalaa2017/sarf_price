from django.urls import path 
from . import views
from .views import CurrencyPricesListView, CurrencyChartsListView, CurrencyConverterListView, GoldChartsListView

from django.contrib.sitemaps import views as sitemap_views
from .sitemaps import ExchangeRatesSitemap

sitemaps = {
    'exchange_rates': ExchangeRatesSitemap,
}

from django.contrib.sitemaps.views import index as sitemap_index
from django.contrib.sitemaps.views import sitemap as sitemap_page



urlpatterns = [
    # sitemaps 
    path('sitemap.xml', sitemap_index, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('sitemap-<section>.xml', sitemap_page, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),


    # api 
    path("api/currencies", CurrencyPricesListView.as_view(), name='api_currencies'),
    path("api/currencies_charts/<str:currency_name>/<str:period>", CurrencyChartsListView.as_view(), name='api_currencies_charts'),
    path("api/gold_charts/<str:gold_name>/<str:period>", GoldChartsListView.as_view(), name='api_gold_charts'), 
    path("api/currencies_converter", CurrencyConverterListView.as_view(), name='api_currencies_converter'),
    path('api/posts/', views.PostListAPIView.as_view(), name='post-list'),


    # Other views
    path('', views.Index_View.as_view(), name="index"),
    path('check', views.check, name="check"),
    path('currencies', views.Currencies_View.as_view(), name="currencies"),
    path('currencies/<str:currency_name>', views.Currencies_Currency_View.as_view(), name="currencies_currency"),

    path('currencies/<str:currency_name>/<str:type>', views.Currencies_Currency_Type_View.as_view(), name="currencies_currency_type"),

    path('gold', views.Gold_View.as_view(), name="gold"),
    path('gold/<str:gold_type>', views.Gold_Details_View.as_view(), name="gold_details"),

    path('fuel', views.Fuel_View.as_view(), name="fuel"),
    path('fuel/<str:fuel_type>', views.Fuel_Details_View.as_view(), name="fuel_details"),
    
    path('news', views.News_View.as_view(), name="news"),
    path('news/<str:post_id>', views.News_Details_View.as_view(), name="news_details"),
    
    path('contact', views.Contact.as_view(), name="contact"),
    path('about', views.About_View.as_view(), name="about"),
    path('privacy_policy', views.Privacy_Policy_View.as_view(), name="privacy_policy"),
    path('terms_conditions', views.Terms_Conditions_View.as_view(), name="terms_conditions"),
]