from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()  #get all the objects from the db

    context = {
        'products': products, # so they available in the template
    }

    return render(request, 'products/products.html', context)