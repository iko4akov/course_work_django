from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from send.models import Send


class SendCreateView(CreateView):
    model = Send
    fields = ['status', 'client', 'period', 'message', 'time']


class SendListView(ListView):
    model = Send


class SendDetailView(DetailView):
    model = Send


class SendUpdateView(UpdateView):
    model = Send

    fields = ['status', 'client', 'period', 'message', 'time']


class SendDeleteView(DeleteView):
    model = Send
