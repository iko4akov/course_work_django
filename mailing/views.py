from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailing.forms import MailingForm
from mailing.models import Mailing


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:list')

    def post(self, request):
        context = {}
        form = self.form_class(request.POST)
        if form.is_valid():
            mailing = form.save(commit=False)
            mailing.user = request.user
            mailing.save()
            context['form'] = form
            return render(request, template_name='mailing/mailing_list.html', context=context)
        return render(request, self.template_name, context)


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ['client', 'send']
    success_url = reverse_lazy('mailing:list')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:list')
