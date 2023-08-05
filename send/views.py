from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from send.models import Send


class SendCreateView(CreateView):
    model = Send
    fields = ['status', 'client', 'period', 'message', 'time']
    success_url = reverse_lazy('send:send_list')


class SendListView(ListView):
    model = Send


class SendDetailView(DetailView):
    model = Send


class SendUpdateView(UpdateView):
    model = Send
    fields = ['status', 'client', 'period', 'message', 'time']
    success_url = reverse_lazy('send:send_list')


class SendDeleteView(DeleteView):
    model = Send
    success_url = reverse_lazy('send:send_list')


def index_view(request):
    context = {}
    context['object_list'] = Send.objects.all()
    return render(request, 'send/list.html', context)
