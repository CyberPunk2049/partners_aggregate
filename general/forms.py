from django import forms
from general.models import Payments,Stores_Categories

category_choices = list(Stores_Categories.objects.values_list('id', 'name'))
payments_choices = list(Payments.objects.values_list('id', 'name'))
category_choices.insert(0,(0,'Все'))
payments_choices.insert(0,(0,'Все'))

class SearchForm(forms.Form):

	search_field = forms.CharField(widget=forms.TextInput(attrs={'class': 'search-input'}))
	choice_payment = forms.ChoiceField(widget=forms.Select(attrs={'class': 'payments-select'}),
	                                   choices=payments_choices)
	choice_category = forms.ChoiceField(widget=forms.Select(attrs={'class': 'category-select'}), choices=category_choices)

