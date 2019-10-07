from django.shortcuts import render,get_object_or_404,redirect
from .forms import UserLoginForm, UserRegisterForm,ProductAddForm
from .models import Ad
from django.contrib import auth
from cart.forms import CartAddProductForm
from django.db.models import Q,F
from django.http import HttpResponseRedirect
# Create your views here.
def main_page(request):
    ads=Ad.objects.all()
    return render(request, 'asserts/html/index.html', locals())
def ad_detail(request,pk):
    ad=get_object_or_404(Ad,pk=pk)
    if ad:
        print('templates/media'+ad.image.url)

        print(ad.views)
        ad.views+=1
        ad.save()
        cart_add=CartAddProductForm()
        context={
            'views': ad.views,
            'user': request.user,
            'id': ad.id,
            'image': ad.image.url,
            'city': ad.city,
            'header':ad.header,
            'description': ad.description,
            'category': ad.category,
            'price': ad.price,
            'card_add' :cart_add
        }
        return render(request, 'asserts/html/ad.html', context)
    else:
        return render(request,'cart/detail.html')

def login_view(request):
    if request.user.is_authenticated:

        return render(request, 'asserts/html/profile.html', {'user':request.user})
    next = request.GET.get('next')

    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        print(user.is_authenticated)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "asserts/html/login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = auth.authenticate(username=user.username, password=password)
        auth.login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "asserts/html/signup.html", context)


def logout_view(request):
    auth.logout(request)
    return redirect('/')


def product_list_view(request):
    category=request.GET.get('category')
    name=request.GET.get('name')
    if name is not None:
        products=Ad.objects.filter(Q(header__icontains=name))
    if category is not None:
        products=Ad.objects.filter(Q(category=category))
    print(products)

    return render(request, 'asserts/html/product_list.html', {'products':products})

def product_add_view(request):
    form=ProductAddForm(request.POST or None)
    if request.POST:

        print(form)
        if form.is_valid():
            print(1)
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'asserts/html/Product_Ad.html', {'form':form})

def new_view(request):
    products=Ad.objects.all()
    cart_add_form=CartAddProductForm()
    electronics=Ad.objects.filter(Q(category='Мобильные/Смартфоны')| Q(category='Компьютеры/Ноутбуки'))
    print(electronics)
    electronics=electronics.order_by('?')
    print(electronics)

    return render(request, 'asserts/html/new.html', {'products':products.order_by('-views'), 'cart_add_form':cart_add_form, 'notebooks_phones':electronics})
