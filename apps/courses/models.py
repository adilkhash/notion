from django.db import models

from django.dispatch import receiver
from qiwi_kassa.models import Invoice
from qiwi_kassa.signals import payment_received
from qiwi_payments.constants import PaymentStatus


class Order(models.Model):
    email = models.EmailField()
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.email


@receiver(payment_received, sender=Invoice)
def payment_handler(sender, **kwargs):
    bill_id = kwargs.get('bill_id')
    invoice = Invoice.objects.get(bill_id=bill_id)
    invoice.status = PaymentStatus.PAID
    invoice.save()
