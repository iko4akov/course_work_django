from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from params.models import Message


class ParamsListView(ListView):
    model = Message


class ParamsDetailView(DetailView):
    model = Message


class ParamsCreateView(CreateView):
    model = Message
    fields = ['time', 'period', 'status', 'message']

    success_url = reverse_lazy('params:params_list')

class ParamsUpdateView(UpdateView):
    model = Message



class ParamsDeleteView(DeleteView):
    model = Message

    success_url = reverse_lazy('params:params_list')
