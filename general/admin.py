from django.contrib import admin
from .models import Banks,Payments,Stores,Stores_Categories
# Register your models here.

class BanksAdmin(admin.ModelAdmin):
	list_display=('name','url','url_bonus','url_stock')
	list_max_show_all=1000
	list_per_page=1000
	search_fields = ['name']

class PaymentsAdmin(admin.ModelAdmin):
	list_display=('name','url','url_bonus','url_stock')
	list_max_show_all=1000
	list_per_page=1000
	search_fields = ['name']

class StoresAdmin(admin.ModelAdmin):
	list_display=('name','categories','url')
	search_fields = ['name','url']
	list_editable=('categories',)

class Stores_CategoriesAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Banks,BanksAdmin)
admin.site.register(Payments,PaymentsAdmin)
admin.site.register(Stores,StoresAdmin)
admin.site.register(Stores_Categories,Stores_CategoriesAdmin)

