# from django.shortcuts import render
from django.views.generic import ListView, DetailView  # импортируем класс получения деталей объекта
from .models import Product
from datetime import datetime


class ProductList(ListView):
    model = Product
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Product.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'new.html'
    context_object_name = 'new'
