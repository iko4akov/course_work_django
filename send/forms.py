from django import forms

from send.models import Send
from client.models import Client

class SendCreateFrom(forms.ModelForm):
    clients = forms.ModelMultipleChoiceField(queryset=Client.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Send
        fields = ['status', 'period', 'message', 'time', 'clients']
