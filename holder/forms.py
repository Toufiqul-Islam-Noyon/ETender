from django import forms
from .models import *


class ApplyTenderForm(forms.ModelForm):
    number = forms.CharField(required=True, label='Tender Fee Payment Phone Number')
    trx_id = forms.CharField(required=True, label='Tender Fee Trans ID')

    class Meta:
        model = ApplyTender
        fields = ['payment_method', 'number', 'trx_id', 'bank_trx_id', 'bank_check_image', 'proposed_amount',
                  'proposal_pdf', 'working_experience']
