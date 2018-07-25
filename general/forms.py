from django import forms
from general.models import Stores_Categories


class BaseSearchForm(forms.Form):
    search_field = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2','placeholder':u'Введите слово','size':'15'})
                                   ,required=False)

class PartnersSearchForm(BaseSearchForm):
    category_choices = tuple(Stores_Categories.objects.values_list('id', 'name'))
    letter_choices = tuple([(i, i) for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'])
    blank_category = (('', '---Категория---'),)
    blank_letter = (('', '---Буква---'),)

    # TODO: Поменять payment на letter
    choice_letter = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                      choices=blank_letter + letter_choices, required=False)
    choice_category = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                        choices=blank_category + category_choices, required=False)
