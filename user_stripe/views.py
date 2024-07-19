# views.py
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def stripe_payment(request):
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        name = request.POST.get('name')
        email = request.POST.get('email')

        try:
            charge = stripe.Charge.create(
                amount=5000,  # Amount in cents
                currency='usd',
                source=token,
                description='Example charge',
                receipt_email=email
            )
            return JsonResponse({'status': 'success'})
        except stripe.error.StripeError as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return render(request, 'index.html')

