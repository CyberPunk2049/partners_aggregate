from django import forms
from django.db.models import Count
from general.forms import BaseSearchForm
from general.models import Banks, Payments


class DiscountSearchForm(BaseSearchForm):
    type_choices = (('All', 'Все'),
                    ('Banks_Stores', 'Банковские скидки'),
                    ('Payments_Stores', 'Скидки платёжных систем'))

    choose_type = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'onchange': 'this.form.submit()'}),
        choices=type_choices,
        initial='All'
    )

    def __init__(self, *args, **kwargs):
        BaseSearchForm.__init__(self, *args, **kwargs)

        if args[0].get('choose_type') == self.type_choices[1][0]:

            self.bank_choices = tuple(
                Banks.objects.annotate(
                    count_partners=Count('partners')
                ).filter(
                    count_partners__gt=0
                ).values_list('id', 'name')
            )
            self.all_banks = (('All', 'Все банки'),)

            self.fields['banks_choice'] = forms.ChoiceField(
                widget=forms.Select(attrs={'class': 'form-control', 'onchange': 'this.form.submit()'}),
                choices=self.all_banks + self.bank_choices, initial='All'
            )

        elif args[0].get('choose_type') == self.type_choices[2][0]:

            self.payment_choices = tuple(Payments.objects.values_list('id', 'name'))
            self.all_payments = (('All', 'Все платёжные системы'),)

            self.fields['payments_choice'] = forms.ChoiceField(
                widget=forms.Select(attrs={'class': 'form-control', 'onchange': 'this.form.submit()'}),
                choices=self.all_payments + self.payment_choices,
                initial='All'
            )
