from django.shortcuts import render
from django.views.generic.list import ListView
from django import forms
from django.db.models import Count, Max

from general.forms import BaseSearchForm,PartnersSearchForm
from general.models import Banks,Stores

class StoresList(ListView):
    '''Класс для отображения списка партнёров'''
    template_name = 'general/stores_list.html'
    queryset = Stores.objects.all()
    default_data={'search_field':'','choice_letter':'','choice_category':''}
    view_name='StoreList'

    def dispatch(self, request, *args, **kwargs):
        if request.GET:
            self.form = PartnersSearchForm(request.GET)
        else:
            self.form = PartnersSearchForm(self.default_data)
        self.form.is_valid()
        return super(StoresList, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StoresList, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StoresList, self).get_context_data(**kwargs)
        context['form'] = self.form
        print(self.form.cleaned_data)
        # Произведем партнёров по полям формы
        if self.form.cleaned_data['search_field']!='':
            self.queryset = self.queryset.filter(name__icontains=self.form.cleaned_data['search_field'])
        if self.form.cleaned_data['choice_letter']!='':
            self.queryset = self.queryset.filter(name__istartswith=self.form.cleaned_data['choice_letter'])
        if self.form.cleaned_data['choice_category']!='':
            self.queryset = self.queryset.filter(categories__id=self.form.cleaned_data['choice_category'])

        context['object_list']=self.queryset.values()
        context['view_name']=self.view_name
        return context


class BanksList(ListView):
    '''Класс для отображения списка банков'''
    template_name = 'general/banks_list.html'
    queryset = Banks.objects.all()
    view_name = 'BanksList'

    def dispatch(self, request, *args, **kwargs):
        self.form = BaseSearchForm(request.GET)
        self.form.is_valid()
        return super(BanksList, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(BanksList, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BanksList, self).get_context_data(**kwargs)
        context['form'] = self.form
        #Произведем фильтрацию банков по полям формы
        self.queryset=self.queryset.filter(name__icontains=self.form.cleaned_data['search_field'])
        #Произведем подсчёт партнёров банков
        self.queryset=self.queryset.annotate(count_partners=Count('partners')).filter(count_partners__gt=0)

        context['object_list']=self.queryset.values()
        context['view_name'] = self.view_name
        return context
