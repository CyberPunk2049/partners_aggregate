from django import forms

from general.forms import BaseSearchForm


class DiscountSearchForm(BaseSearchForm):
    type_choices = ((u'All',u'Все'),
                    (u'Banks_Stores',u'Банковские скидки'),
                    (u'Payments_Stores',u'Скидки платёжных систем'))

    choose_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                      choices=type_choices, required=False)