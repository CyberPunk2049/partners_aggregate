from django.views.generic import TemplateView
from django.db.models import F

from discounts.models import Banks_Stores, Payments_Stores
from discounts.forms import DiscountSearchForm

class DiscountsList(TemplateView):
    '''Класс для отображения найденных скидок'''
    template_name = 'discounts/discounts_list.html'
    view_name = 'DiscountsList'
    empty_messages={
        'nothing':'По вашему запросу ничего не найдено',
        'enterfields':'Введите данные поиска'
    }

    def get(self, request, *args, **kwargs):
        self.form = DiscountSearchForm(request.GET)
        self.form.is_valid()
        context = self.get_context_data(request=request)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(DiscountsList, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['view_name'] = self.view_name
        context['empty_message']=self.empty_messages['nothing']

        if len(kwargs['request'].GET.dict().keys())==0 or self.form.has_changed() == False:
            context['empty_message']=self.empty_messages['enterfields']
            return context

        if 'choose_type' in self.form.changed_data:
            #TODO:Переделать под одно название поля для сервиса
            if 'banks_choice' in self.form.changed_data and 'banks_choice' in kwargs['request'].GET.dict().keys() \
                    or 'payments_choice' in self.form.changed_data and 'payments_choice' in kwargs['request'].GET.dict().keys() \
                    or self.form.cleaned_data['search_field']:
                context['discount_list']=self.get_discount_list(self.form.cleaned_data['choose_type'],kwargs['request'])
            else:
                context['empty_message']=self.empty_messages['enterfields']

            return context

        context['discount_list']=self.get_joint_discount_list(kwargs['request'])

        return context

    def get_joint_discount_list(self,request):
        #объединим списки скидок в один
        type_names = {
            'Banks_Stores':'Банковские скидки',
            'Payments_Stores':'Скидки платёжных систем'
        }
        joint_discount_list=None

        for key,value in type_names.items():
            if joint_discount_list==None:
                joint_discount_list=self.get_discount_list(key,request)
            else:
                joint_discount_list=joint_discount_list.union(self.get_discount_list(key,request))
        return joint_discount_list

    def get_discount_list(self, type_name,request):
        #получим список скидок в зависимости от сервиса
        if type_name == 'Banks_Stores':
            queryset = Banks_Stores.objects.all()
            if 'banks_choice' in self.form.changed_data and 'banks_choice' in request.GET.dict().keys():
                queryset = queryset.filter(id_bank=self.form.cleaned_data['banks_choice'])
            if self.form.cleaned_data['search_field']:
                queryset = queryset.filter(id_store__name__icontains=self.form.cleaned_data['search_field'])
            discount_list = queryset.annotate(service_name=F('id_bank__name'),url_stock=F('id_bank__url_stock')).values('service_name','id_store__name','date_end','url_discount','stock_value','url_stock')
        if type_name == 'Payments_Stores':
            queryset = Payments_Stores.objects.all()
            if 'payments_choice' in self.form.changed_data and 'payments_choice' in request.GET.dict().keys():
                queryset = queryset.filter(id_payment=self.form.cleaned_data['payments_choice'])
            if self.form.cleaned_data['search_field']:
                queryset = queryset.filter(id_store__name__icontains=self.form.cleaned_data['search_field'])
            discount_list = queryset.annotate(service_name=F('id_payment__name'),url_stock=F('id_payment__url_stock')).values('service_name','id_store__name','date_end','url_discount','stock_value','url_stock')

        return discount_list
