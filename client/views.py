from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from client.forms import ClientForm
from client.models import Client


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('first_name', 'second_name', 'third_name', 'email', 'comment')

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        self.success_url = reverse_lazy('client:detail', kwargs={'pk': pk})
        return super().form_valid(form)


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client

    success_url = reverse_lazy('client:list')
