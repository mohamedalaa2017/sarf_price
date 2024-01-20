from django.contrib import admin

from .models import Currency, Currency_Prices, Gold, Gold_Types, Fuel_Types, Fuel, Foreign_Currency, Post, About, Terms_Conditions ,Privacy_Policy, Links, MetaDetails
from ckeditor.widgets import CKEditorWidget
from django.db import models
from django import forms

# Register your models here.

admin.site.site_header = 'Exchangeify'



admin.site.register(Currency)
admin.site.register(Currency_Prices)
admin.site.register(Foreign_Currency)
admin.site.register(Gold)
admin.site.register(Gold_Types)
admin.site.register(Fuel_Types)
admin.site.register(Fuel)



class ChangeTextField(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }

class PostAdmin(admin.ModelAdmin):
    form = PostForm


admin.site.register(Post, PostAdmin)
admin.site.register(About, ChangeTextField)
admin.site.register(Terms_Conditions, ChangeTextField)
admin.site.register(Privacy_Policy, ChangeTextField)
admin.site.register(MetaDetails)

admin.site.register(Links)