from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from features.models import Feature
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    #get two forms information
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
        #create instance of cart, empty if none
            cart = request.session.get('cart', {})
            total = 0
            #check each item in the cart
            for id, quantity in cart.items():
                feature = get_object_or_404(Feature, pk=id)
                #calculate total
                total += quantity * feature.price
                # set up line details
                order_line_item = OrderLineItem(
                    order=order,
                    feature=feature,
                    quantity=quantity
                )
                order_line_item.save()
            #try make payment
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
                if customer.paid:
                    for id, quantity in cart.items():
                        feature = Feature.objects.get(id=id)
                        #increase vote
                        feature.vote += quantity
                        feature.save()
                    messages.success(request, "You have successfully paid")
                    request.session['cart'] = {}
                    return redirect(reverse('features'))
                else:
                    messages.error(request, "Unable to take payment")
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
        else:
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})


