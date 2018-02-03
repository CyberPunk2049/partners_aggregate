from django.contrib import admin
from stocks.models import Stocks,PaymentsStocks


class PaymentsStocksAdmin(admin.ModelAdmin):
	list_display = ('PaymentName', 'StoreName', 'stock_value')
	list_editable = ('stock_value',)

class StocksAdmin(admin.ModelAdmin):
    list_display = ('BankName', 'StoreName', 'stock_value')
    list_editable = ('stock_value',)

admin.site.register(Stocks,StocksAdmin)
admin.site.register(PaymentsStocks,PaymentsStocksAdmin)

