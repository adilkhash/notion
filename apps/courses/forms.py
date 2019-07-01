from django import forms


class InvoiceForm(forms.Form):
    email = forms.EmailField(required=True)
