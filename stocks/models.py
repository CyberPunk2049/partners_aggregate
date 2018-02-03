from django.db import models
from general.models import Banks,Stores,Payments

class Stocks(models.Model):
    id_bank = models.ForeignKey(
        Banks,
        on_delete=models.CASCADE,
        verbose_name='Название банка'
    )
    id_store = models.ForeignKey(
        Stores,
        on_delete=models.CASCADE,
        verbose_name='Партнёр банка'
    )
    stock_value = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='Скидка до,%'
    )

    def BankName(self):
        return self.id_bank

    def StoreName(self):
        return self.id_store

    class Meta:
        verbose_name = u'Скидка партнёра'
        verbose_name_plural = u'Скидки партнёров'
        db_table= 'general_banks_stores_stocks'


class PaymentsStocks(models.Model):
    id_payment = models.ForeignKey(
        Payments,
        on_delete=models.CASCADE,
        verbose_name='Название банка'
    )
    id_store = models.ForeignKey(
        Stores,
        on_delete=models.CASCADE,
        verbose_name='Партнёр банка'
    )
    stock_value = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='Скидка до,%'
    )

    def PaymentName(self):
        return self.id_payment

    def StoreName(self):
        return self.id_store

    class Meta:
        verbose_name = u'Скидка платёжной системы'
        verbose_name_plural = u'Скидки платёжных систем'
        db_table= 'general_payments_stores_stocks'

# Create your models here.
