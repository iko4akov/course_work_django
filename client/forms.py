from django import forms

from client.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'second_name', 'third_name', 'email', 'comment')
