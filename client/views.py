from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from client.forms import ClientForm
from client.models import Client


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        pk = self.request.user.pk
        queryset = super().get_queryset().filter(user=pk)
        return queryset


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.user != self.request.user:
            raise Http404

        return object


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('first_name', 'second_name', 'third_name', 'email', 'comment')

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        self.success_url = reverse_lazy('client:detail', kwargs={'pk': pk})
        return super().form_valid(form)

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.user != self.request.user:
            raise Http404

        return object


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client

    success_url = reverse_lazy('client:list')

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.user != self.request.user:
            raise Http404

        return object
