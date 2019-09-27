from django.shortcuts import render,get_object_or_404,redirect
from .forms import UserLoginForm, UserRegisterForm,ProductAddForm
from .models import Ad
from django.contrib import auth
from cart.forms import CartAddProductForm
from django.http import HttpResponseRedirect
# Create your views here.
def main_page(request):
    ads=Ad.objects.all()
    return render(request,'index.html',locals())
def ad_detail(request,pk):
    ad=get_object_or_404(Ad,pk=pk)
    print('templates/media'+ad.image.url)
    cart_add=CartAddProductForm()
    context={
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
    return render(request,'ad.html',context)


def login_view(request):
    if request.user.is_authenticated:

        return render(request,'profile.html',{'user':request.user})
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
    return render(request, "login.html", context)


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
    return render(request, "signup.html", context)


def logout_view(request):
    auth.logout(request)
    return redirect('/')


def product_list_view(request):
    filter=request.GET.get('filter')
    print(filter)
    products=Ad.objects.filter(category=filter)
    print(products)

    return render(request,'product_list.html',{'products':products})

def product_add_view(request):
    form=ProductAddForm(request.POST or None)
    if request.POST:

        print(form)
        if form.is_valid():
            print(1)
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'Product_Ad.html',{'form':form})
