from django.contrib import admin
from .models import Stock, BuyStock, Broker
# Register your models here.
admin.site.site_header = "MY STOCKS"


class StockAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_share', 'total_price', 'total_investment']


class BuyStockAdmin(admin.ModelAdmin):
    list_display = ['stock', 'total_average_price', 'total_investment']


class BrokerAdmin(admin.ModelAdmin):
    list_display = ['name', 'website']


admin.site.register(Stock, StockAdmin)
admin.site.register(BuyStock, BuyStockAdmin)
admin.site.register(Broker)
