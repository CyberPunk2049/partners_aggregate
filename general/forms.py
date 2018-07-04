from django import forms
from general.models import Payments, Stores_Categories


class SearchForm(forms.Form):
    category_choices = tuple(Stores_Categories.objects.values_list('id', 'name'))
    letter_choices = tuple([(i, i) for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'])
    blank_category = (('', '---Категория---'),)
    blank_letter = (('', '---Буква---'),)

    search_field = forms.CharField(widget=forms.TextInput(attrs={'class': 'search-input'}),required=False)
    # TODO: Поменять payment на letter
    choice_letter = forms.ChoiceField(widget=forms.Select(attrs={'class': 'payments-select'}),
                                      choices=blank_letter + letter_choices,required=False)
    choice_category = forms.ChoiceField(widget=forms.Select(attrs={'class': 'category-select'}),
                                        choices=blank_category + category_choices,required=False)
