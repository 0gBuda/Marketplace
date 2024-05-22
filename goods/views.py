from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from goods.forms import ProductForm
from goods.models import Products
from goods.utils import q_search
from users.models import User


@login_required
def add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProductForm()
    return render(request, 'goods/add.html', {'form': form})


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_id):
    product = Products.objects.get(id=product_id)

    context = {
        "product": product
    }
    return render(request, 'goods/product.html', context)


