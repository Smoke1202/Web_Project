from django.urls import path
from .views import ProductList, ProductDetail, search, NewsDetailView, NewsCreateView, NewsDeleteView, NewsUpdateView


urlpatterns = [
    path('', ProductList.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
    path('search', search),
    path('<int:pk>/', NewsDetailView.as_view()),
    path('create/', NewsCreateView.as_view()),
    path('delete/<int:pk>', NewsDeleteView.as_view()),
    path('update/<int:pk>', NewsUpdateView.as_view()),
]
