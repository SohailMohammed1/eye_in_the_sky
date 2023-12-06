from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe

@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    #Setup
    wh_secret = settings.STRIPE.WH.wh_secret
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signatures 
    payload = request.body
    event = None

    try:
        event = stripe.Webhook.construct_from(
        json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except Exception as e: 
        return HttpResponse(content=e, status=400)

    print('Success!')
    return HttpResponse(status=200)
    

