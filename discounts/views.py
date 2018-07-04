from django.views.generic import TemplateView
from django import forms

from discounts.models import Banks_Stores, Payments_Stores
from discounts.forms import DiscountSearchForm

from general.forms import SearchForm

class DiscountsList(TemplateView):
    '''Класс для отображения найденных скидок'''
    template_name = 'discounts/discounts_list.html'
    view_name = 'DiscountsList'

    def dispatch(self, request, *args, **kwargs):
        self.form = SearchForm(request.GET)
        self.form.fields['choice_letter'].widget = forms.HiddenInput()
        self.form.fields['choice_category'].widget = forms.HiddenInput()
        self.form.is_valid()
        return super(DiscountsList, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DiscountsList, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DiscountsList, self).get_context_data(**kwargs)
        context['form'] = self.form

        if self.form.cleaned_data['search_field']:
            context['discount_dict'] = self.get_dict_of_discount_lists(self.form.cleaned_data['search_field'])
            if True in list(map(bool,context['discount_dict'].values())):
                context['discounts_no_found'] = False
            else:
                context['discounts_no_found'] = True
        context['view_name']=self.view_name
        return context

    def get_dict_of_discount_lists(self, filter_name):
        type_names = {
            'Banks_Stores':'Банковские скидки',
            'Payments_Stores':'Скидки платёжных систем'
        }
        discount_dict={}

        for key,value in type_names.items():
            discount_dict[value]=self.get_discount_list(key,filter_name)

        return discount_dict

    def get_discount_list(self, type_name, filter_name):

        if type_name == 'Banks_Stores':
            queryset = Banks_Stores.objects.filter(id_store__name__icontains=filter_name)
            discount_list = queryset.values_list('id_bank__name', 'id_store__name', 'stock_value')

        if type_name == 'Payments_Stores':
            queryset = Payments_Stores.objects.filter(id_store__name__icontains=filter_name)
            discount_list = queryset.values_list('id_payment__name', 'id_store__name', 'stock_value')

        return discount_list
