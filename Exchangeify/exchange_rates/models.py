from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.


# currency 
class Currency(models.Model):
    country = models.CharField(max_length=64, unique=True, null=True, blank=True)
    country_ar = models.CharField(max_length=64, unique=True, null=True, blank=True)
    name = models.CharField(max_length=64, unique=True, null=True, blank=True)
    name_ar = models.CharField(max_length=64, unique=True, null=True, blank=True)

    image = models.ImageField(upload_to="20%y/%m/%d", null=True, blank=True)
    abbreviation = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.abbreviation

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currency'
    



class Currency_Prices(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="currency_currency_prices")
    exchange_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="exchange_currency_currency_prices")
    buy_market_price = models.FloatField(null=True, blank=True)
    sell_market_price = models.FloatField(null=True, blank=True)
    market_change = models.CharField(max_length=64)
    market_prev_close = models.CharField(max_length=64)
    market_day_range = models.CharField(max_length=64)
    buy_bank_price = models.FloatField(null=True, blank=True)
    sell_bank_price = models.FloatField(null=True, blank=True)
    bank_change = models.CharField(max_length=64)
    bank_prev_close = models.CharField(max_length=64)
    bank_day_range = models.CharField(max_length=64)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if  self.created_at:
            # Use timezone for 'Africa/Cairo'
            # self.created_at = timezone.now().astimezone(timezone.get_current_timezone())

            existing_objects = Currency_Prices.objects.filter(
                created_at__date=self.created_at.date(),
                currency__name=self.currency.name,
                currency__abbreviation=self.currency.abbreviation,
                exchange_currency__name=self.exchange_currency.name,
                exchange_currency__abbreviation=self.exchange_currency.abbreviation,
            )

            # If the current object is not in the existing objects (for an update), remove them
            existing_objects.exclude(pk=self.pk).delete()

        super().save(*args, **kwargs)


    def __str__(self):
        # return str(self.currency.abbreviation)
        return f"{self.pk}-{self.currency.abbreviation}/{self.exchange_currency.abbreviation} ({self.created_at.strftime('%d|%m|%Y')})"

    class Meta:
        verbose_name = 'Currency_Prices'
        verbose_name_plural = 'Currencies_Prices'



class Foreign_Currency(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="currency_foreign")
    exchange_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="currency_exchange_foreign") 
    rate = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if  self.created_at:
        # Use timezone for 'Africa/Cairo'
            self.created_at = timezone.now().astimezone(timezone.get_current_timezone())

            existing_objects = Foreign_Currency.objects.filter(
                created_at__date=self.created_at.date(),
                currency__name=self.currency.name,
                currency__abbreviation=self.currency.abbreviation,
                exchange_currency__name=self.exchange_currency.name,
                exchange_currency__abbreviation=self.exchange_currency.abbreviation,
            )

            # If the current object is not in the existing objects (for an update), remove them
            existing_objects.exclude(pk=self.pk).delete()

        super().save(*args, **kwargs)


# gold
class Gold_Types(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    name_ar = models.CharField(max_length=64, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Karat'
        verbose_name_plural = 'Karat'


class Gold(models.Model):
    karat = models.ForeignKey(Gold_Types, on_delete=models.CASCADE, related_name="gold")
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="gold_currency")
    buy_price = models.FloatField(null=True, blank=True)
    sell_price = models.FloatField(null=True, blank=True)
    change = models.CharField(max_length=64, null=True, blank=True)
    prev_close = models.CharField(max_length=64, null=True, blank=True)
    day_range = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now())


    def save(self, *args, **kwargs):
        if self.created_at:
            # self.created_at = timezone.now().astimezone(timezone.get_current_timezone())

            existing_objects = Gold.objects.filter(
                created_at__date=self.created_at.date(),
                karat__name=self.karat.name,
                currency__name=self.currency.name,
                currency__abbreviation=self.currency.abbreviation,
            )
            
            # If the current object is not in the existing objects (for an update), remove them
            existing_objects.exclude(pk=self.pk).delete()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk}-{self.karat}/{self.buy_price} ({self.created_at.strftime('%d|%m|%Y')})"
    

    class Meta:
        verbose_name = 'Gold'
        verbose_name_plural = 'Gold'


# fuel 
class Fuel_Types(models.Model):
    name = models.CharField(max_length=64)
    name_ar = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fuel_Types'
        verbose_name_plural = 'Fuel_Types'
    
    

class Fuel(models.Model):
    fuel = models.ForeignKey(Fuel_Types, on_delete=models.CASCADE, related_name="fuel_types")
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="fuel_currency")
    buy_price = models.FloatField(null=True, blank=True)
    sell_price = models.FloatField(null=True, blank=True)
    change = models.CharField(max_length=64, null=True, blank=True)
    prev_close = models.CharField(max_length=64, null=True, blank=True)
    day_range = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now())

    def save(self, *args, **kwargs):
        if self.created_at:
            # self.created_at = timezone.now().astimezone(timezone.get_current_timezone())

            existing_objects = Fuel.objects.filter(
                created_at__date=self.created_at.date(),
                currency__name=self.currency.name,
                currency__abbreviation=self.currency.abbreviation,
                fuel__name= self.fuel.name,
            )
            
            # If the current object is not in the existing objects (for an update), remove them
            existing_objects.exclude(pk=self.pk).delete()

        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Fuel'
        verbose_name_plural = 'Fuel'
    
    def __str__(self):
        return f"{self.pk}-{self.fuel} | ({self.created_at.strftime('%d|%m|%Y')})"



#######################################

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="20%y/%m/%d")
    content = models.TextField()
    meta_description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.title} | ({self.created_at.strftime('%d|%m|%Y')})"


class About(models.Model):
    about = models.TextField()
    about_ar = models.TextField()

    created_at = models.DateTimeField(default=datetime.now())

    def save(self, *args, **kwargs):
        if self.created_at:
            existing_objects = About.objects.all()
            existing_objects.exclude(pk=self.pk).delete()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"about added |({self.created_at.strftime('%d|%m|%Y')})"
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Terms_Conditions(models.Model):
    terms_conditions = models.TextField()
    terms_conditions_ar = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())

    def save(self, *args, **kwargs):
        if self.created_at:
            existing_objects = Terms_Conditions.objects.all()
            existing_objects.exclude(pk=self.pk).delete()

        super().save(*args, **kwargs)


    def __str__(self):
        return f"Terms_Conditions added |({self.created_at.strftime('%d|%m|%Y')})"
    

    class Meta:
        verbose_name = 'Terms_Conditions'
        verbose_name_plural = 'Terms_Conditions'




class Privacy_Policy(models.Model):
    privacy_policy = models.TextField()
    privacy_policy_ar = models.TextField()

    created_at = models.DateTimeField(default=datetime.now())

    def save(self, *args, **kwargs):
        if self.created_at:
            existing_objects = Terms_Conditions.objects.all()
            existing_objects.exclude(pk=self.pk).delete()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Privacy_Policy added |({self.created_at.strftime('%d|%m|%Y')})"


    class Meta:
        verbose_name = 'Privacy_Policy'
        verbose_name_plural = 'Privacy_Policy'


class Links(models.Model):
    facebook = models.CharField(max_length=1000)
    telegram = models.CharField(max_length=1000)
    contact_us_email = models.CharField(max_length=1000)

    created_at = models.DateTimeField(default=datetime.now())

    def save(self, *args, **kwargs):
        if self.created_at:
            existing_objects = Terms_Conditions.objects.all()
            existing_objects.exclude(pk=self.pk).delete()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Privacy_Policy added |({self.created_at.strftime('%d|%m|%Y')})"


    class Meta:
        verbose_name = 'links'
        verbose_name_plural = 'links'


class MetaDetails(models.Model):
    index = models.TextField()
    index_ar = models.TextField()

    currencies= models.TextField()
    currencies_ar = models.TextField()

    gold = models.TextField()
    gold_ar = models.TextField()

    fuel= models.TextField()
    fuel_ar = models.TextField()

    news_ar = models.TextField()


    class Meta:
        verbose_name = 'meta details'
        verbose_name_plural = 'meta details'

