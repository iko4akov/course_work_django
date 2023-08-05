from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from client.models import Client


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('first_name', 'second_name', 'third_name', 'email', 'comment')

    success_url = reverse_lazy('client:client_list')


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('first_name', 'second_name', 'third_name', 'email', 'comment')

    success_url = reverse_lazy('client:client_list')


class ClientDeleteView(DeleteView):
    model = Client

    success_url = reverse_lazy('client:client_list')
