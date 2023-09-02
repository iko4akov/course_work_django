from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailing.forms import MailingForm
from mailing.models import Mailing


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list')

    def form_valid(self, form):
        form.instance.user = self.request.user

        pk = self.kwargs.get('pk')
        self.success_url = reverse_lazy('mailing:list', kwargs={'pk': pk})

        return super().form_valid(form)


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ['client', 'send']

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        self.success_url = reverse_lazy('mailing:list', kwargs={'pk': pk})

        return super().form_valid(form)


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:list')
