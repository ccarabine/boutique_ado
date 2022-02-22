from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()  #get all the objects from the db

    context = {
        'products': products, # so they available in the template
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual products """

    product = get_object_or_404(Product,pk=product_id)

    context = {
        'product': product, # so they available in the template
    }

    return render(request, 'products/product_detail.html', context)