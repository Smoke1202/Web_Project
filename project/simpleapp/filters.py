from django.template.backends import django
from django_filters import FilterSet, DateFilter
import django.forms
from .models import Product


class PostFilter(FilterSet):
    date_time = DateFilter(
        lookup_expr='gt',
        widget=django.forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'category__name': ['contains'],
            'author__name': ['contains'],
        }
