from django.apps import AppConfig


class GeneralConfig(AppConfig):
    name = 'general'
    verbose_name='Основной'

class DiscountsConfig(AppConfig):
    name = 'discounts'
    verbose_name='Скидки'