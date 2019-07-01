import decimal

from qiwi_payments.kassa import QiwiKassa
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings

from apps.courses.forms import InvoiceForm


def create_luigi_invoice(request):
    form = InvoiceForm(request.POST)
    if form.is_valid():
        kassa = QiwiKassa(settings.QIWI_KASSA_SECRET_KEY)
        invoice = kassa.create_bill(
            amount=decimal.Decimal('690.00'),
            currency='RUB',
            comment='For the Luigi course'
        )
        return HttpResponseRedirect(invoice.pay_url)
    else:
        return HttpResponse('Неверно введён адрес электронной почты')
