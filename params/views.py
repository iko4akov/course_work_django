from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from params.models import Params


class ParamsListView(ListView):
    model = Params


class ParamsDetailView(DetailView):
    model = Params


class ParamsCreateView(CreateView):
    model = Params
    fields = ['time', 'period', 'status', 'message']

    success_url = reverse_lazy('params:params_list')


class ParamsUpdateView(UpdateView):
    model = Params


class ParamsDeleteView(DeleteView):
    model = Params

    success_url = reverse_lazy('params:params_list')
