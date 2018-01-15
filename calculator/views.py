from django.shortcuts import render
from django.http import HttpResponse
from dal import autocomplete
from calculator.models import Food
from django import forms
from django.template import loader
from django.utils.safestring import mark_safe
import json


def index(request):
    pseudo_data = mark_safe(list(Food.objects.values_list('name', flat=True)))
    data = Food.objects.all()
    template = loader.get_template('calculator/main.html')
    context = {
        "food_data" : pseudo_data,
        "data" : data
    }
    return HttpResponse(template.render(context, request))


class FoodAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Food.objects.none()

        qs = Food.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('__all__')
        widgets = {'kcal': autocomplete.ModelSelect2(url='food-autocomplete')}