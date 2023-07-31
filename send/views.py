from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from send.models import Send


class SendCreateView(CreateView):
    model = Send

    fields = ['params', 'client']

    success_url = 'send:send_list'

class SendListView(ListView):
    model = Send


class SendDetailView(DetailView):
    model = Send


class SendUpdateView(UpdateView):
    model = Send

    fields = ['params.period', 'client']


class SendDeleteView(DeleteView):
    model = Send
