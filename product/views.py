from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Product


def product_list(request):
    products = Product.objects.all()
    # all이라도 붙여줘야함
    return render(request, 'product/product_list.html', {'products': products})

