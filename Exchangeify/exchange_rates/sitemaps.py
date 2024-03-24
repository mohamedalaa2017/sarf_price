from django.contrib.sitemaps import Sitemap
from django.urls import reverse, NoReverseMatch

class ExchangeRatesSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        excluded_patterns = ['/api/']
        valid_urls = []
        for name in self.get_named_urlpatterns():
            try:
                url = reverse(name)
                valid_urls.append(url)
            except NoReverseMatch:
                pass
        return valid_urls

    def location(self, item):
        return item

    @staticmethod
    def get_named_urlpatterns():
        from .urls import urlpatterns
        named_patterns = []
        for pattern in urlpatterns:
            if hasattr(pattern, 'name') and pattern.name:
                named_patterns.append(pattern.name)
        return named_patterns
