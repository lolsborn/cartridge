import stripe

from django.utils.datastructures import MultiValueDictKeyError 
from mezzanine.conf import settings

from cartridge.shop.checkout import CheckoutError
from stripe import InvalidRequestError

stripe.api_key = settings.STRIPE_SECRET


def process(request, order_form, order):
    amount = order.total
    if request.method == "POST":
        try:
            print request.POST['stripeToken']
            token = request.POST['stripeToken']
            charge = stripe.Charge.create(
                amount=int(amount * 100), # amount in cents, again
                currency="usd",
                card=token,
                description=order,
            )
            return charge
        except (MultiValueDictKeyError, InvalidRequestError):
            CheckoutError("There was an error")

    else:
        CheckoutError("There was an error")


# def create_stripe_customer(token,request):
# 	customer = stripe.Customer.create(
# 	    card=token,
# 	    description=request.user,
# 	)
# 	return customer

# def get_customer(request):
# 	if request.user.get_profile().stripe_customer:
# 		customer = request.user.get_profile().stripe_customer
# 		return customer

# def save_customer(request,customer):
# 	request.user.get_profile().stripe_customer = customer
# 	request.user.get_profile().save()

# def pay_customer(request, customer):

# 	amount = request.POST['amount'] * 100 #in dollars to cents
# 	if request.method == "POST":
# 		charge = stripe.Charge.create(
# 		    amount=amount, # amount in cents, again
# 		    currency="usd",
# 		    customer=customer,
# 		    description=request.user,
# 		)
# 		print 'success'
# 		return charge