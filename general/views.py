from django.shortcuts import render
from django.http import JsonResponse
from general.models import Banks, Stores, Payments
from django.db.models import Count, Avg
from general.forms import SearchForm


def banks(request):
	params_form=SearchForm()
	context = {'form':params_form}
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


def partners_calculate(request):
	debug_mode = False

	if request.is_ajax():
		print(request.session)
		stores_id = request.GET['storesid']
		bank_store_list = Stores.objects.filter(banks__id=request.GET['id']).values_list('id', flat=True)
		response = JsonResponse(list(bank_store_list), safe=False)
		return response


	else:
		if (debug_mode == True):
			stores_id = [
				3,
				4,
				5,
				6,
				7,
				8,
				9,
				10,
				11,
				12,
				13,
				14
			]
		else:
			if 'storesid' in request.POST:
				stores_id = request.POST['storesid']
				if len(stores_id) > 2:
					stores_id = stores_id[1:-1]
					stores_id = stores_id.split(',')
					stores_id = list(map(int, stores_id))
				else:
					stores_id = []
			else:
				stores_id = []

		client_store_list = Stores.objects.filter(id__in=stores_id)
		bank_list = Banks.objects.filter(partners__in=client_store_list).annotate(num_partners=Count('partners'),avg_stocks=Count('partners'))
		context = {
			'bank_list': bank_list,
			'store_list': client_store_list
		}
		response = render(request, 'partners_calculate.html', context)
		return response


def partners_selector(request):
	stores_id = request.POST['storesid']
	if len(stores_id) > 2:
		stores_id = stores_id[1:-1]
		stores_id = stores_id.split(',')
		print(len(stores_id))
		stores_id = list(map(int, stores_id))
	else:
		stores_id = []

	store_list = Stores.objects.all()
	context = {
		'client_store_list': stores_id,
		'store_list': store_list
	}
	response = render(request, 'partners_selector.html', context)
	return response


def bank_info():
	pass
