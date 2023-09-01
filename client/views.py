from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from client.forms import ClientForm
from client.models import Client


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('first_name', 'second_name', 'third_name', 'email', 'comment')

    def form_valid(self, form):
        pk = self.request.cliet.pk
        self.success_url = reverse_lazy('client:detail', kwargs={'pk': pk})
        return super().form_valid(form)




class ClientDeleteView(DeleteView):
    model = Client

    success_url = reverse_lazy('client:list')
