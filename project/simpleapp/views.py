from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Product
from datetime import datetime
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import ProductForm


class ProductList(ListView):
    model = Product
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Product.objects.order_by('-date_time')
    paginate_by = 3

    def get_context(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs


def search(request):
    f = PostFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'search.html', {'filter': f})


class ProductDetail(DetailView):
    model = Product
    template_name = 'new.html'
    context_object_name = 'new'


class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    queryset = Product.objects.all()


class NewsCreateView(CreateView):
    template_name = 'news_create.html'
    form_class = ProductForm
    success_url = '/news/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)


class NewsUpdateView(UpdateView):
    template_name = 'news_create.html'
    form_class = ProductForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)


class NewsDeleteView(DeleteView):
    template_name = 'news_delete.html'
    queryset = Product.objects.all()
    context_object_name = 'new'
    success_url = '/news/'