from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class ExchangeRatesSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return ['index', 'currencies', 'gold', 'fuel', 'news', 'contact', 'about', 'privacy_policy', 'terms_conditions']

    def location(self, item):
        return reverse(item)