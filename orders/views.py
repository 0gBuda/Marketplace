from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import render, redirect

from carts.models import Cart
from .forms import CreateOrderForm
from .models import Order, OrderItem


def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_item = Cart.objects.filter(user=user)

                    if cart_item.exists():
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data["requires_delivery"],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )

                        for item in cart_item:
                            product = item.product
                            name = item.product.name
                            quantity = item.quantity
                            price = item.product.sell_price()

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточно {name} в наличии\
                                    В наличии {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                quantity=quantity,
                                price=price,
                                name=name,
                            )

                            product.quantity -= quantity
                            product.save()

                        cart_item.delete()

                        messages.success(request, 'Заказ успешно оформлен')
                        return redirect('users:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('orders:order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = CreateOrderForm(initial=initial)

    context = {
        'form': form,
        'order': True,
    }
    return render(request, 'orders/create_order.html', context)
