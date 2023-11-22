from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from products.models import Product
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
  # Import your Product model here

def view_bag(request):
    """ A view to render bag content page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product in the shopping bag """
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id, None)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

def remove_from_bag(request, item_id):
    """Remove the specified product from the shopping bag."""
    
    bag = request.session.get('bag', {})

    try:
        item_id_str = str(item_id)  # Convert item_id to string
        if item_id_str in bag:
            bag.pop(item_id_str)  # Remove the item from the bag
            request.session['bag'] = bag  # Update the session bag
            request.session.modified = True  # Mark the session as "modified" to make sure it gets saved
            messages.success(request, "Item removed from your bag.")
        else:
            messages.error(request, "Item not found in your bag.")
    except Exception as e:
        messages.error(request, f"Error removing item: {e}")

    return redirect('view_bag')  

    

