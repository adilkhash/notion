import decimal

from qiwi_kassa.models import Invoice
from qiwi_payments.kassa import QiwiKassa
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings

from apps.courses.forms import InvoiceForm
from apps.courses.models import Order


def create_luigi_invoice(request):
    form = InvoiceForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        kassa = QiwiKassa(settings.QIWI_KASSA_SECRET_KEY)
        invoice = kassa.create_bill(
            amount=decimal.Decimal('690.00'),
            currency='RUB',
            comment=f'invoice for {email}'
        )
        invoice = Invoice.objects.create(
            bill_id=invoice.bill_id,
            amount=invoice.amount.value,
            currency=invoice.amount.currency,
            payment_url=invoice.pay_url,
            expiration_dt=invoice.expiration_dt,
            status=invoice.status.value
        )
        Order.objects.create(
            email=email,
            invoice=invoice
        )
        return HttpResponseRedirect(invoice.payment_url)
    else:
        return HttpResponse('Неверно введён адрес электронной почты')
