import re
from .models import MetaDetails
class CurrencyInfoNav:
    def __init__(self, currency_price, not_currency=False):
        

        self.information = currency_price
        if not_currency:
            self.percentage, self.value_in_parentheses = self.extract_percentage_and_value(currency_price.change)
        else:
            self.market_percentage, self.market_value_in_parentheses = self.extract_percentage_and_value(currency_price.market_change)
            self.bank_percentage, self.bank_value_in_parentheses = self.extract_percentage_and_value(currency_price.bank_change)


    def extract_percentage_and_value(self, change):
        # print("the change is " + change)
        if not isinstance(change, str):
            return '', ''
        pattern = re.compile(r'([+-]?\d*\.\d+)%\s*\(([-+]?\d+(\.\d+)?)\)')
        match = pattern.match(change)

        if match:
            percentage = f'%{match.group(1)}'
            value_in_parentheses = f'({match.group(2)})'
        else:
            percentage = ''
            value_in_parentheses = ''

        return percentage, value_in_parentheses

    
class MetaInfo:
    def __init__(self):
        self.index = self.extract_meta_description("index")
        self.index_ar = self.extract_meta_description("index")

        self.currencies = self.extract_meta_description("currencies")
        self.currencies_ar = self.extract_meta_description("currencies_ar")

        self.fuel = self.extract_meta_description("fuel")
        self.fuel_ar = self.extract_meta_description("fuel_ar")

        self.gold = self.extract_meta_description("gold")
        self.gold_ar = self.extract_meta_description("gold_ar")


    def extract_meta_description(self, change):
        MetaDetails.objects.filter().last()
        
