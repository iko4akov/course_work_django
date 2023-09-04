from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailing.forms import MailingForm
from mailing.models import Mailing


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing

    def get_queryset(self):
        pk = self.request.user.pk
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=pk)
        return queryset




class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.user != self.request.user:
            raise Http404

        return object


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    fields = ['client', 'send']

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        self.success_url = reverse_lazy('mailing:list', kwargs={'pk': pk})

        return super().form_valid(form)

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.user != self.request.user:
            raise Http404

        return object


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:list')

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.user != self.request.user:
            raise Http404

        return object
