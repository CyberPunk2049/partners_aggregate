from django import forms

class DiscountSearchForm(forms.Form):
    search_field = forms.CharField(required=False)