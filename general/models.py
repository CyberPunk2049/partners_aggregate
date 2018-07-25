from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

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
        verbose_name='Сайт',
        validators=[
            URLValidator,
                    ],
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

    def clean(self):

        # При сохранении нового партнёра проверяет, есть ли партнёры с таким URL в базе данных.
        # Вызывает исключение со списком имён партнёров, у которых совпадает URL.
        if self.id==None:
            if self.url !='':
                url=self.url.split('/')[2]
                db_stores_all=Stores.objects.values_list('name','url')
                db_stores_url=[(k,i.split('/')[2]) for (k,i) in db_stores_all if i!='']
                urls_names=[i for (k,i) in db_stores_url]
                if url in urls_names:
                    overlap_names=[k for (k,i) in db_stores_url if i==url]
                    raise ValidationError('Партнёры: '+','.join(overlap_names)+' - имеют схожий URL')
        else:
            urls_names = [i.split('/')[2] for
                          i in Stores.objects.exclude(id=self.id).values_list('url', flat=True) if i != '']
            if self.url!='' and self.url.split('/')[2] in urls_names :
                raise ValidationError('The URL already exists in database')
    class Meta:
        verbose_name = u'Партнёр'
        verbose_name_plural = u'Партнёры'
        ordering = ('name',)


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
    url_bonus = models.URLField(        max_length=300,
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
        through='discounts.Banks_Stores',
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
        through='discounts.Payments_Stores',
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
