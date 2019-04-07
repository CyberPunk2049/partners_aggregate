from django.contrib import admin
from discounts.models import Banks_Stores, Payments_Stores


class PaymentsStocksAdmin(admin.ModelAdmin):
    list_display = ('id_payment', 'id_store', 'stock_value', 'url_discount', 'date_end')
    list_editable = ('stock_value', 'date_end')
    search_fields = ['id_payment__name', 'id_store__name']


class StocksAdmin(admin.ModelAdmin):
    list_display = ('id_bank', 'id_store', 'stock_value', 'url_discount', 'date_end')
    list_editable = ('stock_value', 'date_end')
    search_fields = ['id_bank__name', 'id_store__name']


admin.site.register(Banks_Stores, StocksAdmin)
admin.site.register(Payments_Stores, PaymentsStocksAdmin)
