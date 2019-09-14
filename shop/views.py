from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect , get_object_or_404
from .forms import *
from panier.forms import CartAddProductForm
# Create your views here.


def homepage(request):
    return render(request,'homepage.html',locals())


def product_page(request):
    return render(request,'ProductDetails.html',locals())



def signup_page(request):
    if request.method == "POST":
        form = signupForm(request.POST or None)
        form2 = utilisateurForm(request.POST or None)

        if form.is_valid() and form2.is_valid():
            print("hello")
            user2 = form.save()
            utilisateur = form2.save()
            utilisateur.save()
            # user2.is_staff = True
            user2.is_active =True
            user2.save()
            utilisateur.user = user2
            utilisateur.save()


            return HttpResponse('confirm your email')
        else:
            print(form.errors)

    else:
        form = signupForm(request.POST or None)
        form2 = utilisateurForm(request.POST or None)
    return render(request, 'signup.html', locals())


def login_page(request):

        if request.method == "POST":
            form = AuthenticationForm(data=request.POST or None)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return render(request,'homepage.html',locals())
            else:
                print(form.errors)
        else:
            form = AuthenticationForm(data=request.POST or None)

        return render(request, 'login.html', locals())


def product_list(request, category_slug=None):
    from .models import Categorie, product

    category = None
    categories = Categorie.objects.all()
    products = product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Categorie, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, product_id, slug):
    from .models import product
    product = get_object_or_404(product,
                                id=product_id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})