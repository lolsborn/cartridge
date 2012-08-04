import stripe
from mezzanine.conf import settings

from cartridge.shop.checkout import CheckoutError

stripe.api_key = settings.STRIPE_SECRET


def process(request, order_form, order):
    amount = order.total
    print amount
    print request.POST['stripeToken']

    if request.method == "POST":
        # import pdb; pdb.set_trace()
        token = request.POST['stripeToken']
        charge = stripe.Charge.create(
            amount= int(amount * 100), # amount in cents, again
            currency="usd",
            card=token,
            description=order.id,
        )
        return charge

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
