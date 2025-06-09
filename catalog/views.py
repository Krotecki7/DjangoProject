from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, TemplateView, DetailView


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product.html"
