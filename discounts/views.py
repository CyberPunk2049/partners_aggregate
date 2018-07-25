from django.views.generic import TemplateView
from django.db.models import F

from discounts.models import Banks_Stores, Payments_Stores
from discounts.forms import DiscountSearchForm

class DiscountsList(TemplateView):
    '''Класс для отображения найденных скидок'''
    template_name = 'discounts/discounts_list.html'
    view_name = 'DiscountsList'

    def dispatch(self, request, *args, **kwargs):
        self.form = DiscountSearchForm(request.GET,initial={'choose_type':'All','search_field':''})
        self.form.is_valid()
        return super(DiscountsList, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DiscountsList, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DiscountsList, self).get_context_data(**kwargs)
        context['form'] = self.form

        if self.form.cleaned_data['search_field']:
            context['joint_discount_list'] = self.get_joint_discount_list(self.form.cleaned_data['search_field'])

        context['view_name']=self.view_name
        print(context['form'].changed_data)
        return context

    def get_joint_discount_list(self, filter_name):
        #объединим списки скидок в один
        type_names = {
            'Banks_Stores':'Банковские скидки',
            'Payments_Stores':'Скидки платёжных систем'
        }
        joint_discount_list=None

        if self.form.cleaned_data['choose_type']=='All':
            for key,value in type_names.items():
                if joint_discount_list==None:
                    joint_discount_list=self.get_discount_list(key,filter_name)
                else:
                    joint_discount_list=joint_discount_list.union(self.get_discount_list(key,filter_name))
        else:
           joint_discount_list = self.get_discount_list(self.form.cleaned_data['choose_type'], filter_name)
        return joint_discount_list

    def get_discount_list(self, type_name, filter_name):
        #получим список скидок в зависимости от сервиса
        if type_name == 'Banks_Stores':
            queryset = Banks_Stores.objects.filter(id_store__name__icontains=filter_name)
            discount_list = queryset.annotate(service_name=F('id_bank__name'),url_stock=F('id_bank__url_stock')).values('service_name','id_store__name', 'stock_value','url_stock')
        if type_name == 'Payments_Stores':
            queryset = Payments_Stores.objects.filter(id_store__name__icontains=filter_name)
            discount_list = queryset.annotate(service_name=F('id_payment__name'),url_stock=F('id_payment__url_stock')).values('service_name','id_store__name', 'stock_value','url_stock')

        return discount_list
