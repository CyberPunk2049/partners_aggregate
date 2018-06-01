from django.views.generic import TemplateView
from discounts.models import Banks_Stores, Payments_Stores
from discounts.forms import DiscountSearchForm

class DiscountsListView(TemplateView):

    template_name = 'discounts/banks_stores_list.html'

    def dispatch(self, request, *args, **kwargs):

        self.form = DiscountSearchForm(request.GET)
        self.form.is_valid()

        return super(DiscountsListView, self).dispatch(request,*args,**kwargs)

    def get(self, request, *args, **kwargs):

        return super(DiscountsListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super(DiscountsListView, self).get_context_data(**kwargs)
        context['form'] = self.form

        if self.form.cleaned_data['search_field']:
            context['discount_dict'] = self.get_dict_of_discount_lists(self.form.cleaned_data['search_field'])
            if True in list(map(bool,context['discount_dict'].values())):
                context['discounts_no_found'] = False
            else:
                context['discounts_no_found'] = True

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
