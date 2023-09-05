from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from send.models import Send


class SendCreateView(LoginRequiredMixin, CreateView):
    model = Send
    fields = ['period', 'message', 'time', ]
    success_url = reverse_lazy('send:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SendListView(LoginRequiredMixin, ListView):
    model = Send

    def get_queryset(self):
        pk = self.request.user.pk
        queryset = super().get_queryset().filter(user=pk)
        return queryset


class SendDetailView(LoginRequiredMixin, DetailView):
    model = Send

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.user != self.request.user:
            raise Http404

        return object


class SendUpdateView(LoginRequiredMixin, UpdateView):
    model = Send
    fields = ['status', 'period', 'message', 'time']

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        self.success_url = reverse_lazy('send:detail', kwargs={'pk': pk})
        return super().form_valid(form)

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.user != self.request.user:
            raise Http404

        return object


class SendDeleteView(LoginRequiredMixin, DeleteView):
    model = Send
    success_url = reverse_lazy('send:list')

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.user != self.request.user:
            raise Http404

        return object
