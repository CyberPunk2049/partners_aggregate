from django.shortcuts import render
from general.forms import SearchForm


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



def bank_info():
    pass
