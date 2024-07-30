from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse
from django.views import View
import stripe
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from payment.models import Plan, UserSubscription

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

def plan_list(request):
    plans = Plan.objects.all()
    return render(request, 'payment/plan_list.html', {'plans': plans})



class PaymentView(View):
    def get(self, request, plan_id):
        plan = Plan.objects.get(id=plan_id)
        context = {
            'plan': plan,
            'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
        }
        return render(request, 'payment/payment.html', context)

    def post(self, request, plan_id):
        plan = Plan.objects.get(id=plan_id)
        token = request.POST.get('stripeToken')
        
        try:
            charge = stripe.Charge.create(
                amount=int(plan.price * 100),
                currency='usd',
                description=f'{plan.name} subscription',
                source=token,
            )

            if charge.status == 'succeeded':
                end_date = timezone.now() + timedelta(days=plan.duration)
                UserSubscription.objects.create(
                    user=request.user,
                    plan=plan,
                    end_date=end_date,
                    active=True
                )
                return redirect('payment:payment_success')
            else:
                return redirect('payment:payment_error')
        except stripe.error.StripeError as e:
            return redirect('payment:payment_error')

@login_required
def payment_success(request):
    return render(request, 'payment/payment_success.html')

@login_required
def payment_error(request, plan_id):
    # Fetch the plan by ID
    plan = get_object_or_404(Plan, id=plan_id)
    return render(request, 'payment/payment_error.html', {'plan': plan})