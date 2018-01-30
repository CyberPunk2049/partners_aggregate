from django.db import models


class Stores_Categories(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='Категория'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


class Stores(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
        unique=True,
        verbose_name='Название'
    )
    url = models.URLField(
        max_length=300,
        blank=True,
        verbose_name='Сайт'
    )
    url_logo = models.URLField(
        max_length=300,
        blank=True,
        editable=False,
        verbose_name='Логотип'
    )

    categories = models.ForeignKey(
        Stores_Categories,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Партнёр'
        verbose_name_plural = u'Партнёры'


class Banks(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    url = models.URLField(
        max_length=300,
        blank=True,
        verbose_name='Сайт'
    )
    url_logo = models.URLField(
        max_length=300,
        blank=True,
        editable=False,
        verbose_name='Логотип'
    )
    url_bonus = models.URLField(
        max_length=300,
        blank=True,
        verbose_name='Ссылка на акции, бонусы и спецпредложения'
    )
    url_stock = models.URLField(
        max_length=300,
        blank=True,
        verbose_name='Ссылка на партнёрские программы'
    )
    partners = models.ManyToManyField(
        Stores,
        through='Stocks',
        related_name='banks'
    )

    def __str__(self):
        return self.name

    def url_href(self):
        return '<a href="' + self.url + '">Ссылка</a>'

    class Meta:
        verbose_name = u'Банк'
        verbose_name_plural = u'Банки'
        ordering = ['name']

class Payments(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    url = models.URLField(
        max_length=300,
        blank=True,
        verbose_name='Сайт'
    )
    url_logo = models.URLField(
        max_length=300,
        blank=True,
        editable=False,
        verbose_name='Логотип'
    )
    url_bonus = models.URLField(
        max_length=300,
        blank=True,
        verbose_name='Ссылка на акции, бонусы и спецпредложения'
    )
    url_stock = models.URLField(
        max_length=300,
        blank=True,
        verbose_name='Ссылка на партнёрские программы'
    )
    partners = models.ManyToManyField(
        Stores,
        through='PaymentsStocks',
        related_name='payments'
    )

    def __str__(self):
        return self.name

    def url_href(self):
        return '<a href="' + self.url + '">Ссылка</a>'

    class Meta:
        verbose_name = u'Платёжная система'
        verbose_name_plural = u'Платёжные системы'
        ordering = ['name']


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