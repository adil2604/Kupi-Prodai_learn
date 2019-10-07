from django.views.decorators.http import require_POST
from Main.models import Ad
from .cart import Cart
from .forms import CartAddProductForm
from django.shortcuts import render, redirect, get_object_or_404


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Ad, id=product_id)
    form = CartAddProductForm(request.POST)
    print(form.errors)
    if form.is_valid():
        cd = form.cleaned_data
        print(cd)
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Ad, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})