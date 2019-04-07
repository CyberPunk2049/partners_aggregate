from django.db import models
from general.models import Banks, Stores, Payments

class Banks_Stores(models.Model):
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
    url_discount = models.URLField(
        max_length=300,
        blank=True,
        verbose_name='Ссылка на скидку'
    )
    date_end = models.DateField(
        default='2099-12-31',
        verbose_name='Срок скидки'
    )

    def __str__(self):
        return self.id_bank.name + ' : ' + self.id_store.name

    class Meta:
        verbose_name = u'Скидку банка'
        verbose_name_plural = u'Скидки банков'
        db_table = 'discounts_banks_stores'
        unique_together = (('id_bank', 'id_store'),)


class Payments_Stores(models.Model):
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
    url_discount = models.URLField(
        max_length=300,
        blank=True,
        verbose_name='Ссылка на скидку'
    )
    date_end = models.DateField(
        default='2099-12-31',
        verbose_name='Срок скидки'
    )

    def __str__(self):
        return self.id_payment.name + ' : ' + self.id_store.name

    class Meta:
        verbose_name = u'Скидку платёжной системы'
        verbose_name_plural = u'Скидки платёжных систем'
        db_table = 'discounts_payments_stores'
        unique_together = (('id_payment', 'id_store'),)
