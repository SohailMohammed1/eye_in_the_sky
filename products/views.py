from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products, 
    }


    return render(request, 'products/product.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Product  # Make sure to import your Product model

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product,  # Change 'products' to 'product'
    }

    return render(request, 'products/product_detail.html', context)
