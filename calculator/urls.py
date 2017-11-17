from django.conf.urls import url
from calculator.views import FoodAutocomplete
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^food-autocomplete/$',
        FoodAutocomplete.as_view(),
        name='food-autocomplete',
    ),
]