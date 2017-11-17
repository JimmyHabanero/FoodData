from django.shortcuts import render
from dal import autocomplete
from calculator.models import Food
from django import forms

def index(request):
    return(render(request, 'calculator/autocomplete.html'))


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