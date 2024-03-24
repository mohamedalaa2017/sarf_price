from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class ExchangeRatesSitemap(Sitemap):       
    changefreq = "daily"
    priority = 0.8

    def items(self):
        # Return the actual view names
        return ['index', 'currencies', 'gold', 'fuel', 'news', 'contact', 'about', 'privacy_policy', 'terms_conditions']

    def location(self, item):
        # Reverse the view name to get the URL
        return reverse(item)
