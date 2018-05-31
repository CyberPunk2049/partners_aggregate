from django.shortcuts import render
from general.forms import SearchForm
from django.views.generic import TemplateView
from django.http.response import HttpResponse
from discounts.models import Banks_Stores, Payments_Stores


def banks(request):
    params_form = SearchForm()
    context = {'form': params_form}
    context['view_name'] = 'banks'
    return render(request, 'banks.html', context)


def partners(request):
    params_form = SearchForm()
    context = {'form': params_form}
    context['view_name'] = 'partners'
    return render(request, 'partners.html', context)


def personal_choice(request):
    params_form = SearchForm()
    context = {'form': params_form}
    context['view_name'] = 'personal_choice'
    return render(request, 'personal_choice.html', context)


class DiscountsListView(TemplateView):
    template_name = 'discounts/banks_stores_list.html'

    def get(self, request, *args, **kwargs):
        return super(DiscountsListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DiscountsListView, self).get_context_data(**kwargs)
        context['discount_list'] = 'list'
        print(self.get_dict_of_discount_lists('агентство'))
        return context

    def get_dict_of_discount_lists(self, filter_name):

        type_names = {
            'Banks_Stores':'Банки',
            'Payments_Stores':'Платёжные системы'
        }
        discount_dict={}

        for key,value in type_names.items():
            discount_dict[value]=self.get_discount_list(key,filter_name)

        return discount_dict



    def get_discount_list(self, type_name, filter_name):
        if type_name == 'Banks_Stores':
            queryset = Banks_Stores.objects.filter(id_store__name__icontains=filter_name)
            discount_list = queryset.values_list('id_bank__name', 'id_store__name')
        if type_name == 'Payments_Stores':
            queryset = Payments_Stores.objects.filter(id_store__name=filter_name)
            discount_list = queryset.values_list('id_payment__name', 'id_store__name')
        return discount_list


def bank_info():
    pass
