from django.contrib import admin
from discounts.models import Banks_Stores,Payments_Stores


class PaymentsStocksAdmin(admin.ModelAdmin):
	list_display = ('PaymentName', 'StoreName', 'stock_value')
	list_editable = ('stock_value',)

class StocksAdmin(admin.ModelAdmin):
    list_display = ('BankName', 'StoreName', 'stock_value')
    list_editable = ('stock_value',)

admin.site.register(Banks_Stores, StocksAdmin)
admin.site.register(Payments_Stores,PaymentsStocksAdmin)

