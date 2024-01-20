from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import activate
from django.utils.translation import gettext as _

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .utils import CurrencyInfoNav

from django.db.models import Max
from django.core.cache import cache  # Import Django cache module

import json
import math

from django.utils import timezone
import pytz

from .models import Currency, Currency_Prices, Gold, Gold_Types, Fuel_Types, Fuel, Foreign_Currency, Post, About, Terms_Conditions ,Privacy_Policy, Links, MetaDetails

from .script import currencies_in_database, gold_in_database, fuel_in_database, foreign_currency_in_database



from rest_framework import generics
from .serializers import CurrencyPricesSerializer, GoldSerializer, PostSerializer
from rest_framework.response import Response


# api 
class CurrencyPricesListView(generics.ListAPIView):
    queryset = Currency_Prices.objects.all()
    serializer_class = CurrencyPricesSerializer

    def get_queryset(self):
        now = timezone.now()
        currencies = Currency_Prices.objects.filter(created_at__date=now.date())

        if not currencies.exists():
            latest_prices = Currency_Prices.objects.values('currency__name').annotate(latest_created_at=Max('created_at')).order_by('latest_created_at')
            currency_names = [item['currency__name'] for item in latest_prices]
            latest_created_ats = [item['latest_created_at'] for item in latest_prices]

            currencies = Currency_Prices.objects.filter(currency__name__in=currency_names, created_at__in=latest_created_ats)
            currencies = list(currencies)
            currencies.reverse()

        return currencies

class CurrencyChartsListView(generics.ListAPIView):
    serializer_class = CurrencyPricesSerializer

    def get_queryset(self):
        currency_name = self.kwargs.get('currency_name')
        period = self.kwargs.get('period')

        if not currency_name or period not in ['today', 'week', 'month', '3months', '6months', 'all']:
            return []

        # Check if the result is already in cache
        cache_key = f"{currency_name}_{period}".replace(" ", "_")
        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data

        # Define a mapping of periods to date filters
        period_filters = {
            'today': timezone.now().date(),
            'week': timezone.now() - timezone.timedelta(days=7),
            'month': timezone.now() - timezone.timedelta(days=30),
            '3months': timezone.now() - timezone.timedelta(days=90),
            '6months': timezone.now() - timezone.timedelta(days=180),
            'year': timezone.now() - timezone.timedelta(days=365),  # One year
            'all': None,  # No date filter for 'all'
        }

        # Get the date filter based on the specified period
        date_filter = period_filters.get(period)

        # Construct the base queryset based on the currency_name
        base_queryset = Currency_Prices.objects.filter(currency__name=currency_name)

        # Apply date filter to the queryset
        if date_filter is not None:
            base_queryset = base_queryset.filter(created_at__date__gte=date_filter)

        # Convert queryset to list to avoid cache serialization issues
        result_list = list(base_queryset)

        # Cache the result for future requests
        cache.set(cache_key, result_list)

        return result_list

class CurrencyConverterListView(generics.ListAPIView):
    queryset = Currency_Prices.objects.all()

    serializer_class = CurrencyPricesSerializer

    
    def get_queryset(self):
        now = timezone.now()
        currencies = Currency_Prices.objects.filter(created_at__date=now.date())

        if not currencies.exists():
            latest_prices = Currency_Prices.objects.values('currency__name').annotate(latest_created_at=Max('created_at')).order_by('-latest_created_at')
            currency_names = [item['currency__name'] for item in latest_prices]

            currencies = Currency_Prices.objects.filter(currency__name__in=currency_names, created_at__in=[item['latest_created_at'] for item in latest_prices]).order_by('-created_at')

        return currencies


    def list(self, request, *args, **kwargs):
        # Get the original response data
        response = super().list(request, *args, **kwargs)

        # Manipulate the data to get the desired format
        currencies = response.data
        formatted_data = [
            {
                "currency": currency['currency']['abbreviation'],
                "buy_market_price": currency['buy_market_price'],
                "sell_market_price": currency['sell_market_price']
            }
            for currency in currencies
        ]

        # Return the formatted data
        return Response(formatted_data)

##
class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        limit = int(self.request.query_params.get('limit', 5))
        offset = int(self.request.query_params.get('offset', 0))
        return Post.objects.all().order_by('-id')[offset:offset + limit]

##

class GoldChartsListView(generics.ListAPIView):
    serializer_class = GoldSerializer

    def get_queryset(self):
        gold_name = self.kwargs.get('gold_name')
        period = self.kwargs.get('period')

        # if not gold_name or period not in ['today', 'week', 'month', '3months', '6months', 'all']:
        #     return []

        # Check if the result is already in cache
        cache_key = f"{gold_name}_{period}".replace(" ", "_")
        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data

        # Define a mapping of periods to date filters
        period_filters = {
            'today': timezone.now().date(),
            'week': timezone.now() - timezone.timedelta(days=7),
            'month': timezone.now() - timezone.timedelta(days=30),
            '3months': timezone.now() - timezone.timedelta(days=90),
            '6months': timezone.now() - timezone.timedelta(days=180),
            'year': timezone.now() - timezone.timedelta(days=365),  # One year
            'all': None,  # No date filter for 'all'
        }

        # Get the date filter based on the specified period
        date_filter = period_filters.get(period)

        # Construct the base queryset based on the gold_name
        base_queryset = Gold.objects.filter(karat__name=gold_name)

        # Apply date filter to the queryset
        if date_filter is not None:
            base_queryset = base_queryset.filter(created_at__date__gte=date_filter)

        # Convert queryset to list to avoid cache serialization issues
        result_list = list(base_queryset)

        # Cache the result for future requests
        cache.set(cache_key, result_list)

        return result_list


################### finish api ##########################





# base views 
class BaseView(View):
    def get_currency_currency_prices(self, currency):
        print(Currency_Prices.objects.filter(currency__name=f'{currency}').last())
        currency_price = Currency_Prices.objects.filter(currency__name=currency).last()
        
        us_dollar = CurrencyInfoNav(currency_price)

        return us_dollar
    
    def get_latest_currency_prices(self):
        now = timezone.now()
        currencies = Currency_Prices.objects.filter(created_at__date=now.date())

        if not currencies:
            currencies = Currency_Prices.objects.all()
            latest_prices = Currency_Prices.objects.values('currency__name').annotate(latest_created_at=Max('created_at')).order_by('latest_created_at')
            currencies = Currency_Prices.objects.filter(currency__name__in=[item['currency__name'] for item in latest_prices], created_at__in=[item['latest_created_at'] for item in latest_prices])
            currencies = list(currencies)
            currencies.reverse()


        return currencies
    
    def get_latest_foreign_currency(self):
        now = timezone.now()
        currencies = Foreign_Currency.objects.filter(created_at__date=now.date())

        if not currencies:
            currencies = Foreign_Currency.objects.all()
            latest_prices = Foreign_Currency.objects.values('currency__name').annotate(latest_created_at=Max('created_at')).order_by('latest_created_at')
            currencies = Foreign_Currency.objects.filter(currency__name__in=[item['currency__name'] for item in latest_prices], created_at__in=[item['latest_created_at'] for item in latest_prices])
            currencies = list(currencies)
            currencies.reverse()

        return currencies
    




    def get_time_egypt_now(self, **kwargs):
        utc_now = timezone.now()
        egypt_tz = pytz.timezone('Africa/Cairo')
        egypt_now = utc_now.astimezone(egypt_tz)
        time_egypt_now = egypt_now.strftime('%Y/%m/%d %H:%M')
        
        return time_egypt_now



    def get_currency_exchange(self, currency):
        cur_now = currency.buy_market_price
        # print(round(cur_now * 1))

        currency_exchange = {
            "1": '{:,}'.format(round(cur_now)),
            "5": '{:,}'.format(round(cur_now * 5)),
            "10": '{:,}'.format(round(cur_now * 10)),
            "25": '{:,}'.format(round(cur_now * 25)),
            "50": '{:,}'.format(round(cur_now * 50)),
            "100": '{:,}'.format(round(cur_now * 100)),
            "500": '{:,}'.format(round(cur_now * 500)),
            "1000": '{:,}'.format(round(cur_now * 1000)),
            "5000": '{:,}'.format(round(cur_now * 5000)),
            "10000": '{:,}'.format(round(cur_now * 10000)),
        }
        return currency_exchange



    # gold 
    def get_latest_gold(self):
        now = timezone.now()
        golds = Gold.objects.filter(created_at__date=now.date())

        if not golds:
            golds = Gold.objects.all()
            latest_prices = Gold.objects.values('karat__name').annotate(latest_created_at=Max('created_at')).order_by('latest_created_at')
            golds = Gold.objects.filter(karat__name__in=[item['karat__name'] for item in latest_prices], created_at__in=[item['latest_created_at'] for item in latest_prices])
            golds = list(golds)
            golds.reverse()

        return golds

    def get_gold_karat_21(self):
        gold_karat_21 = Gold.objects.filter(karat__name="21Karat").last()
        karat_21 = CurrencyInfoNav(gold_karat_21, True)

        return karat_21

    

    def get_gold_ounce(self):
        ounce = Gold.objects.filter(karat__name="Gold Ounce").last()
        ounce = CurrencyInfoNav(ounce, True)

        return ounce
    
    # fuel 
    def get_latest_fuel(self):
        now = timezone.now()
        fuels = Fuel.objects.filter(created_at__date=now.date())

        if not fuels:
            fuels = Fuel.objects.all()
            latest_fuels = Fuel.objects.values('fuel__name').annotate(latest_created_at=Max('created_at')).order_by('latest_created_at')
            fuels = Fuel.objects.filter(fuel__name__in=[item['fuel__name'] for item in latest_fuels], created_at__in=[item['latest_created_at'] for item in latest_fuels])
            fuels = list(fuels)
            fuels.reverse()

        return fuels
    
    def get_octane_95(self):
        # return Fuel.objects.filter(fuel__name="Octane 95").last() 
        fuel_95 = Fuel.objects.filter(fuel__name="Octane 95").last() 
        fuel_95 = CurrencyInfoNav(fuel_95, True)

        return fuel_95
    
    def get_solar(self):
        solar = Fuel.objects.filter(fuel__name="Solar").last()
        solar = CurrencyInfoNav(solar, True)

        return solar


    #links 
    def get_links(self):
        return Links.objects.all().last()
    
    #meta 
    def get_meta(self):
        return MetaDetails.objects.all().last()




# finish base views #####
        



# class view .
def check(request):
    return render(request, "exchange_rates/trying.html", {

})

class Index_View(BaseView):
    def get(self, request):

        golds = self.get_latest_gold()
        fuels = self.get_latest_fuel()
        foreign_currencies = self.get_latest_foreign_currency()
        posts = Post.objects.all().order_by('-id')



        us_dollar_currency_prices = self.get_currency_currency_prices("US Dollar")
        euro_currency_prices = self.get_currency_currency_prices("Euro")
        gold_karat_21 = self.get_gold_karat_21()
        gold_ounce = self.get_gold_ounce()
        octane_95 =self.get_octane_95()
        solar = self.get_solar()
        links = self.get_links()
        meta_details = self.get_meta()


        currencies = self.get_latest_currency_prices()


        time_egypt_now = self.get_time_egypt_now()

    

        return render(request, "exchange_rates/index.html", {

            "currencies": currencies,

            "time_egypt_now": time_egypt_now, 

            "golds": golds,
            "fuels": fuels,
            "posts": posts,
            
            "foreign_currencies": foreign_currencies,

            "us_dollar_currency_prices": us_dollar_currency_prices,
            "euro_currency_prices": euro_currency_prices, 
            "gold_karat_21": gold_karat_21,
            "gold_ounce": gold_ounce,
            "octane_95":  octane_95,
            "solar": solar,
            "links": links,
            "meta_details": meta_details
      
        })




class Currencies_View(BaseView):
    def get(self, request):
        us_dollar_currency_prices = self.get_currency_currency_prices("US Dollar")
        euro_currency_prices = self.get_currency_currency_prices("Euro")
        gold_karat_21 = self.get_gold_karat_21()
        gold_ounce = self.get_gold_ounce()

        currencies = self.get_latest_currency_prices()
        currencies_json = json.dumps(currencies, default=str)
        octane_95 =self.get_octane_95()
        solar = self.get_solar()
        links = self.get_links()
        meta_details = self.get_meta()



        return render(request, "exchange_rates/currencies.html", {
            "currencies": currencies,
            "currencies_json": currencies_json, 

            "us_dollar_currency_prices": us_dollar_currency_prices,
            "euro_currency_prices": euro_currency_prices, 
            "gold_karat_21": gold_karat_21,
            "gold_ounce": gold_ounce,
            "octane_95":  octane_95,
            "solar": solar,
            "links": links,
            "meta_details": meta_details

    })
        


class Currencies_Currency_View(BaseView):
    def get(self, request, currency_name):
        if not (currency := Currency_Prices.objects.filter(currency__name=currency_name).last()):
            return HttpResponseRedirect(reverse("currencies"))
        
        currency_exchange = self.get_currency_exchange(currency)
        time_egypt_now = self.get_time_egypt_now


        us_dollar_currency_prices = self.get_currency_currency_prices("US Dollar")
        euro_currency_prices = self.get_currency_currency_prices("Euro")
        gold_karat_21 = self.get_gold_karat_21()
        gold_ounce = self.get_gold_ounce()

        octane_95 =self.get_octane_95()
        solar = self.get_solar()
        links = self.get_links()
        meta_details = self.get_meta()




        return render(request, "exchange_rates/currencies_currency.html", {
            "currency": currency,
            "currency_exchange": currency_exchange, 
            "time_egypt_now": time_egypt_now, 

            "us_dollar_currency_prices": us_dollar_currency_prices,
            "euro_currency_prices": euro_currency_prices, 
            "gold_karat_21": gold_karat_21,   
            "gold_ounce": gold_ounce, 
            "octane_95":  octane_95,
            "solar": solar,  
            "links": links, 
            "meta_details": meta_details   
        })
    

class Currencies_Currency_Type_View(BaseView):
    def get(self, request, currency_name, type):
        # if currency not exist
        if not (currency := Currency_Prices.objects.filter(currency__name=currency_name).last()):
            return HttpResponseRedirect(reverse("currencies"))
        


        # if type not market or bank
        if type not in ["market", "bank"]:
            return HttpResponseRedirect(reverse("currencies_currency", kwargs={'currency_name': currency_name}))

        if type == "bank":
                currency_price = currency.buy_bank_price
        elif type == "market":
            currency_price = currency.buy_market_price

        
        us_dollar_currency_prices = self.get_currency_currency_prices("US Dollar")
        euro_currency_prices = self.get_currency_currency_prices("Euro")
        gold_karat_21 = self.get_gold_karat_21()
        gold_ounce = self.get_gold_ounce()
        octane_95 =self.get_octane_95()
        solar = self.get_solar()
        links = self.get_links()
        meta_details = self.get_meta()



        
        currency_exchange = self.get_currency_exchange(currency)

        return render(request, "exchange_rates/currencies_currency_type.html", {
            "currency": currency,
            "currency_exchange": currency_exchange, 
            "type": type,

            "us_dollar_currency_prices": us_dollar_currency_prices,
            "euro_currency_prices": euro_currency_prices, 
            "gold_karat_21": gold_karat_21,      
            "gold_ounce": gold_ounce,
            "octane_95":  octane_95,
            "solar": solar,
            "links": links, 
            "meta_details": meta_details

     
            
        })


class Gold_View(BaseView):
    def get(self, request):

        golds = self.get_latest_gold()

        us_dollar_currency_prices = self.get_currency_currency_prices("US Dollar")
        euro_currency_prices = self.get_currency_currency_prices("Euro")
        gold_karat_21 = self.get_gold_karat_21()
        gold_ounce = self.get_gold_ounce()
        octane_95 =self.get_octane_95()
        solar = self.get_solar()
        links = self.get_links()
        meta_details = self.get_meta()






        
        return render(request, "exchange_rates/gold.html", {
            "golds": golds,
            "us_dollar_currency_prices": us_dollar_currency_prices,
            "euro_currency_prices": euro_currency_prices, 
            "gold_karat_21": gold_karat_21,
            "gold_ounce": gold_ounce,
            "octane_95":  octane_95,
            "solar": solar,
            "links": links,
            "meta_details": meta_details
    })


class Gold_Details_View(BaseView):
    def get(self, request, gold_type):
        if not (gold := Gold.objects.filter(karat__name=gold_type).first()):
            return HttpResponseRedirect(reverse("gold"))
        
        
        us_dollar_currency_prices = self.get_currency_currency_prices("US Dollar")
        euro_currency_prices = self.get_currency_currency_prices("Euro")
        gold_karat_21 = self.get_gold_karat_21()
        gold_ounce = self.get_gold_ounce()
        octane_95 =self.get_octane_95()
        solar = self.get_solar()
        links = self.get_links()
        meta_details = self.get_meta()


        return render(request, "exchange_rates/gold_details.html", {
            "gold": gold,
            "us_dollar_currency_prices": us_dollar_currency_prices,
            "euro_currency_prices": euro_currency_prices, 
            "gold_karat_21": gold_karat_21,
            "gold_ounce": gold_ounce, 
            "octane_95":  octane_95,
            "solar": solar,
            "links": links,
            "meta_details": meta_details
        })



class Fuel_View(BaseView):
    def get(self, request):

        fuels = self.get_latest_fuel()
        
        us_dollar_currency_prices = self.get_currency_currency_prices("US Dollar")
        euro_currency_prices = self.get_currency_currency_prices("Euro")
        gold_karat_21 = self.get_gold_karat_21()
        gold_ounce = self.get_gold_ounce()

        octane_95 =self.get_octane_95()
        solar = self.get_solar()
        links = self.get_links()
        meta_details = self.get_meta()

        return render(request, "exchange_rates/fuel.html", {
            "fuels": fuels,

            "us_dollar_currency_prices": us_dollar_currency_prices,
            "euro_currency_prices": euro_currency_prices,
            "gold_karat_21": gold_karat_21,        
            "gold_ounce": gold_ounce,
            "octane_95":  octane_95,
            "solar": solar, 
            "links": links,
            "meta_details": meta_details      
    })


class Fuel_Details_View(BaseView):
    def get(self, request, fuel_type):

        if not (fuel := Fuel.objects.filter(fuel__name=fuel_type).first()):
            return HttpResponseRedirect(reverse("fuel"))


        us_dollar_currency_prices = self.get_currency_currency_prices("US Dollar")
        euro_currency_prices = self.get_currency_currency_prices("Euro")
        gold_karat_21 = self.get_gold_karat_21()
        gold_ounce = self.get_gold_ounce()
        octane_95 =self.get_octane_95()
        solar = self.get_solar()
        links = self.get_links()
        meta_details = self.get_meta()

        
        return render(request, "exchange_rates/fuel_details.html", {
            "fuel" : fuel,
            "us_dollar_currency_prices": us_dollar_currency_prices,
            "euro_currency_prices": euro_currency_prices, 
            "gold_karat_21": gold_karat_21,
            "gold_ounce": gold_ounce,
            "octane_95":  octane_95,
            "solar": solar,
            "links": links,
            "meta_details": meta_details

        })


class News_View(BaseView):
    def get(self, request):

        news = Post.objects.all()


        us_dollar_currency_prices = self.get_currency_currency_prices("US Dollar")
        euro_currency_prices = self.get_currency_currency_prices("Euro")
        gold_karat_21 = self.get_gold_karat_21()
        gold_ounce = self.get_gold_ounce()
        octane_95 =self.get_octane_95()
        solar = self.get_solar()
        links = self.get_links()
        meta_details = self.get_meta()


        return render(request, "exchange_rates/news.html", {
            "news": news,

            "us_dollar_currency_prices": us_dollar_currency_prices,
            "euro_currency_prices": euro_currency_prices, 
            "gold_karat_21": gold_karat_21,
            "gold_ounce": gold_ounce,
            "octane_95":  octane_95,
            "solar": solar,
            "links": links,
            "meta_details": meta_details
        })




class News_Details_View(BaseView):
    def get(self, request, post_id):
        if not (post := Post.objects.filter(id=post_id).first()):
            return HttpResponseRedirect(reverse("news"))
        

        us_dollar_currency_prices = self.get_currency_currency_prices("US Dollar")
        euro_currency_prices = self.get_currency_currency_prices("Euro")
        gold_karat_21 = self.get_gold_karat_21()
        gold_ounce = self.get_gold_ounce()
        octane_95 =self.get_octane_95()
        solar = self.get_solar()
        links = self.get_links()
        meta_details = self.get_meta()

        return render(request, "exchange_rates/news_details.html", {
            "post": post,

            "us_dollar_currency_prices": us_dollar_currency_prices,
            "euro_currency_prices": euro_currency_prices, 
            "gold_karat_21": gold_karat_21,
            "gold_ounce": gold_ounce,
            "octane_95":  octane_95,
            "solar": solar,  
            "links": links,
            "meta_details": meta_details

        })
        






class Contact(BaseView):
    def get(self, request):
        us_dollar_currency_prices = self.get_currency_currency_prices("US Dollar")
        euro_currency_prices = self.get_currency_currency_prices("Euro")
        gold_karat_21 = self.get_gold_karat_21()
        gold_ounce = self.get_gold_ounce()
        octane_95 =self.get_octane_95()
        solar = self.get_solar()
        links = self.get_links()
        meta_details = self.get_meta()


        return render(request, "exchange_rates/contact.html", {

            "us_dollar_currency_prices": us_dollar_currency_prices,
            "euro_currency_prices": euro_currency_prices, 
            "gold_karat_21": gold_karat_21,
            "gold_ounce": gold_ounce,
            "octane_95":  octane_95,
            "solar": solar,
            "links": links,
            "meta_details": meta_details
      
        })

    

class About_View(BaseView):
    def get(self, request):
        about = About.objects.all().last()

        us_dollar_currency_prices = self.get_currency_currency_prices("US Dollar")
        euro_currency_prices = self.get_currency_currency_prices("Euro")
        gold_karat_21 = self.get_gold_karat_21()
        gold_ounce = self.get_gold_ounce()
        octane_95 =self.get_octane_95()
        solar = self.get_solar()
        links = self.get_links()
        meta_details = self.get_meta()


        return render(request, "exchange_rates/about_as.html", {
            "about": about,

            "us_dollar_currency_prices": us_dollar_currency_prices,
            "euro_currency_prices": euro_currency_prices, 
            "gold_karat_21": gold_karat_21,
            "gold_ounce": gold_ounce,
            "octane_95":  octane_95,
            "solar": solar,  
            "links": links,
            "meta_details": meta_details
            
        })

    

class Privacy_Policy_View(BaseView):
    def get(self, request):
        privacy_policy = Privacy_Policy.objects.all().last()
        print(privacy_policy)

        us_dollar_currency_prices = self.get_currency_currency_prices("US Dollar")
        euro_currency_prices = self.get_currency_currency_prices("Euro")
        gold_karat_21 = self.get_gold_karat_21()
        gold_ounce = self.get_gold_ounce()
        octane_95 =self.get_octane_95()
        solar = self.get_solar()
        links = self.get_links()
        meta_details = self.get_meta()

        return render(request, "exchange_rates/privacy_policy.html", {
            "privacy_policy": privacy_policy,

            "us_dollar_currency_prices": us_dollar_currency_prices,
            "euro_currency_prices": euro_currency_prices, 
            "gold_karat_21": gold_karat_21,
            "gold_ounce": gold_ounce,
            "octane_95":  octane_95,
            "solar": solar, 
            "links": links,
            "meta_details": meta_details      
        })

    


class Terms_Conditions_View(BaseView):
    def get(self, request):
        terms_conditions = Terms_Conditions.objects.all().last()
        us_dollar_currency_prices = self.get_currency_currency_prices("US Dollar")
        euro_currency_prices = self.get_currency_currency_prices("Euro")
        gold_karat_21 = self.get_gold_karat_21()
        gold_ounce = self.get_gold_ounce()
        octane_95 =self.get_octane_95()
        solar = self.get_solar()
        links = self.get_links()
        meta_details = self.get_meta()

        return render(request, "exchange_rates/terms_conditions.html", {
            "terms_conditions": terms_conditions,

            "us_dollar_currency_prices": us_dollar_currency_prices,
            "euro_currency_prices": euro_currency_prices, 
            "gold_karat_21": gold_karat_21,
            "gold_ounce": gold_ounce,
            "octane_95":  octane_95,
            "solar": solar,  
            "links": links,
            "meta_details": meta_details       
        })

    



